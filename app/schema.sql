CREATE TABLE IF NOT EXISTS test_results (
    id          BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name        TEXT        NOT NULL,
    status      TEXT        NOT NULL CHECK (status IN ('pass', 'failed', 'skipped')),
    date        TIMESTAMPTZ NOT NULL DEFAULT now(),
    duration    NUMERIC(10, 3) NOT NULL CHECK (duration >= 0)
);
