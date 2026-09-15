# Transactional Outbox Pattern — Example

A Python + PostgreSQL example implementation of the **transactional outbox pattern**, used in distributed systems to reliably dispatch messages/events as part of a database transaction rather than risking a dual-write failure between the DB and a message broker.

## Components

- **Outbox** — the outbox table in the database; provides a method to insert a message into it as part of the same transaction as the business write.
- **OutboxMessage** — a message inserted into the outbox (content, destination, metadata).
- **MessageDispatcher** — polls the outbox for pending messages, dispatches them, and marks them as dispatched on success.

## Prerequisites

- Python 3.x
- PostgreSQL

## Setup

```bash
pip install psycopg2
```

Apply the schema in [`database.sql`](database.sql) to your PostgreSQL instance, then run [`transactional_outbox.py`](transactional_outbox.py).

## Slides

[`software architecture.pptx`](software%20architecture.pptx) — presentation covering the pattern and this implementation.

> The example is packaged as `transactional_outbox_project.rar` in this repo — extract it to get `transactional_outbox.py`, `database.sql`, and the slide deck.
