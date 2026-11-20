CREATE TABLE IF NOT EXISTS test_results (
    id          BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    test_id     UUID        NOT NULL,
    test_path   TEXT        NOT NULL,
    test_module TEXT        NOT NULL,
    test_name   TEXT        NOT NULL,
    status      TEXT        NOT NULL CHECK (status IN ('passed', 'failed', 'skipped')),
    date        TIMESTAMPTZ NOT NULL DEFAULT now(),
    duration    NUMERIC(10, 3) NOT NULL CHECK (duration >= 0)
);
