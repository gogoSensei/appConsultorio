/*
CREATE TABLE usuarios(
  id       SERIAL PRIMARY KEY,
  nombre   TEXT NOT NULL,
  email    TEXT NOT NULL,
  password TEXT NOT NULL,
  activo   BOOLEAN,
  fecha    DATE,
  arr      TEXT[]
);

CREATE TABLE logusers(
  id SERIAL PRIMARY KEY,
  emailUser TEXT,
  fechareal TIMESTAMP DEFAULT now(),
  arr       TEXT[]
);

INSERT INTO usuarios VALUES(DEFAULT, 
                            'isidro',
                            'isidro.rm.88@gmail.com', 
                            'd6395c595e41775e54947e9f8639470d',
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


