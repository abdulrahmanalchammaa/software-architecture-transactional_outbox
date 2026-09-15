the file type of : CREATE TABLE outbox (
    id SERIAL PRIMARY KEY,
    content TEXT,
    destination TEXT,
    metadata TEXT,
    created_at TIMESTAMP DEFAULT NOW(),
    dispatched BOOLEAN DEFAULT FALSE
);
