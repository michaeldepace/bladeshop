DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS product;
DROP TABLE IF EXISTS cart;
DROP TABLE IF EXISTS user_order;


CREATE TABLE user (
  usr_id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE product (
    prd_id INTEGER PRIMARY KEY AUTOINCREMENT,
    prd_name TEXT NOT NULL,
    prd_category TEXT
);

CREATE TABLE cart (
    crt_id INTEGER PRIMARY KEY AUTOINCREMENT,
    usr_id INTEGER NOT NULL,
    prd_id INTEGER NOT NULL,
    prd_amount INTEGER NOT NULL
)

-- CREATE TABLE user_order(
--     ordr_id INTEGER PRIMARY KEY AUTOINCREMENT,

-- )


-- DROP TABLE IF EXISTS post;
-- CREATE TABLE post (
--   id INTEGER PRIMARY KEY AUTOINCREMENT,
--   author_id INTEGER NOT NULL,
--   created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
--   title TEXT NOT NULL,
--   body TEXT NOT NULL,
--   FOREIGN KEY (author_id) REFERENCES user (id)
-- );
