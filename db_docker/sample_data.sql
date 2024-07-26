BEGIN;
CREATE TABLE IF NOT EXISTS public.api_user
(
    id       SERIAL
        PRIMARY KEY,
    email    VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);

ALTER TABLE public.api_user
    OWNER TO postgres;

CREATE UNIQUE INDEX IF NOT EXISTS user_email
    ON public.api_user (email);

CREATE TABLE IF NOT EXISTS public.location
(
    id   SERIAL
        PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

ALTER TABLE public.location
    OWNER TO postgres;

CREATE TABLE IF NOT EXISTS public.device
(
    id          SERIAL
        PRIMARY KEY,
    type        VARCHAR(255) NOT NULL,
    login       VARCHAR(255) NOT NULL,
    password    VARCHAR(255) NOT NULL,
    location_id INTEGER      NOT NULL
        REFERENCES public.location
            ON DELETE RESTRICT,
    api_user_id INTEGER      NOT NULL
        REFERENCES public.api_user
            ON DELETE RESTRICT
);

ALTER TABLE public.device
    OWNER TO postgres;

CREATE INDEX IF NOT EXISTS device_location_id
    ON public.device (location_id);

CREATE INDEX IF NOT EXISTS device_api_user_id
    ON public.device (api_user_id);

INSERT INTO api_user (email, password)
VALUES ('john.doe@example.com', 'password123'),
       ('jane.smith@example.com', 'securepassword'),
       ('alice.jones@example.com', 'password321'),
       ('bob.brown@example.com', 'mypassword'),
       ('charlie.wilson@example.com', 'password456');


INSERT INTO location (name)
VALUES ('New York'),
       ('San Francisco'),
       ('Chicago'),
       ('Los Angeles'),
       ('Seattle');

INSERT INTO device (type, login, password, location_id, api_user_id)
VALUES ('Laptop', 'laptop_user1', 'laptop_pass1',
        (SELECT id FROM location WHERE name = 'New York'),
        (SELECT id FROM api_user WHERE email = 'john.doe@example.com')),
       ('Smartphone', 'smartphone_user2', 'smartphone_pass2',
        (SELECT id FROM location WHERE name = 'San Francisco'),
        (SELECT id FROM api_user WHERE email = 'jane.smith@example.com')),
       ('Tablet', 'tablet_user3', 'tablet_pass3',
        (SELECT id FROM location WHERE name = 'Chicago'),
        (SELECT id FROM api_user WHERE email = 'alice.jones@example.com')),
       ('Desktop', 'desktop_user4', 'desktop_pass4',
        (SELECT id FROM location WHERE name = 'Los Angeles'),
        (SELECT id FROM api_user WHERE email = 'bob.brown@example.com')),
       ('Smartwatch', 'smartwatch_user5', 'smartwatch_pass5',
        (SELECT id FROM location WHERE name = 'Seattle'),
        (SELECT id FROM api_user WHERE email = 'charlie.wilson@example.com'));

COMMIT;