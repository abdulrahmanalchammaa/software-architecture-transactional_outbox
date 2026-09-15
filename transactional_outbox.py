import datetime
import psycopg2

class OutboxMessage:
    def __init__(self, content, destination, metadata):
        self.content = content
        self.destination = destination
        self.metadata = metadata

class Outbox:
    def __init__(self, connection_string):
        self.connection_string = connection_string

    def insert_message(self, message):
        try:
            # Open a connection to the database
            conn = psycopg2.connect(self.connection_string)
            cursor = conn.cursor()

            # Insert the message into the outbox table
            query = "INSERT INTO outbox (content, destination, metadata, created_at) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (message.content, message.destination, message.metadata, datetime.datetime.now()))

            # Commit the transaction
            conn.commit()

        except (Exception, psycopg2.Error) as error:
            print("Error inserting message into outbox:", error)

        finally:
            # Close the database connection
            if conn:
                cursor.close()
                conn.close()

class MessageDispatcher:
    def __init__(self, connection_string):
        self.connection_string = connection_string

    def dispatch_messages(self):
        try:
            # Open a connection to the database
            conn = psycopg2.connect(self.connection_string)
            cursor = conn.cursor()

            # Retrieve pending messages from the outbox table
            query = "SELECT id, content, destination, metadata FROM outbox WHERE dispatched = false"
            cursor.execute(query)
            messages = cursor.fetchall()

            for message in messages:
                # Simulate message dispatching
                print("Dispatching message:", message[1])

                # Update the message as dispatched
                update_query = "UPDATE outbox SET dispatched = true WHERE id = %s"
                cursor.execute(update_query, (message[0],))

                # Commit the transaction
                conn.commit()

        except (Exception, psycopg2.Error) as error:
            print("Error dispatching messages:", error)

        finally:
            # Close the database connection
            if conn:
                cursor.close()
                conn.close()

# Usage example
if __name__ == '__main__':
    # Connection string to the PostgreSQL database
    connection_string = "dbname=mydatabase user=myuser password=mypassword host=localhost port=5432"

    # Create an instance of the Outbox
    outbox = Outbox(connection_string)

    # Insert a message into the outbox
    message = OutboxMessage("Hello, world!", "destination_service", "metadata")
    outbox.insert_message(message)

    # Create an instance of the MessageDispatcher
    dispatcher = MessageDispatcher(connection_string)

    # Dispatch pending messages
    dispatcher.dispatch_messages()
