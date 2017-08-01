CREATE TABLE usuarios(
  id       SERIAL PRIMARY KEY,
  nombre   TEXT,
  email    TEXT,
  password TEXT,
  activo   BOOLEAN,
  fecha    DATE,
  arr      TEXT[]
);

INSERT INTO usuarios VALUES(DEFAULT, 
                            'isidro',
                            'isidro.rm.88@gmail.com', 
                            'af819e17df8167186a7b168f8f6aaeb377e5bbb591588f60bddc10da',
                            TRUE,
                            NOW()::DATE,
                            NULL);
