/*
CREATE TABLE usuarios(
  id       SERIAL PRIMARY KEY,
  nombre   TEXT NOT NULL,
  email    TEXT PRIMARY KEY,
  password TEXT NOT NULL,
  activo   BOOLEAN,
  fecha    DATE,
  arr      TEXT[],
);


INSERT INTO usuarios VALUES(DEFAULT, 
                            'isidro',
                            'isidro.rm.88@gmail.com', 
                            'af819e17df8167186a7b168f8f6aaeb377e5bbb591588f60bddc10da',
                            TRUE,
                            NOW()::DATE,
                            NULL);
*/

-- IRM 06/08/2017 Funcion de login para los usuarios
CREATE OR REPLACE FUNCTION gr_login_user(p_usuarios TEXT, p_password TEXT)
  RETURNS BOOLEAN as $$
DECLARE
  rm     RECORD;
  _pass  TEXT := md5(p_password);
BEGIN
  SELECT INTO rm * FROM usuarios WHERE email = p_usuarios;
  IF (rm.email = (p_usuarios) AND rm.password = _pass) THEN
    RETURN TRUE;
  END IF;
  RETURN FALSE;
END;$$
LANGUAGE plpgsql;
  