--=======================================================================================
--
-- INTEGRANTES:
-- Bryan Stiven Tabarez Mestra	- 1131782
-- Aurelio Antonio Vivas Meza	- 1110348
-- George Romero Ramirez		- 1130924
--
--=======================================================================================
-- Area
-- Cama
-- Persona
-- Paciente
-- Empleado
-- Medico
-- Enfermera
-- Habilidad
-- Enfermera_Habilidad
-- Cama_Paciente
-- Historia_clinica
-- Horario_Consulta
-- Cita
-- Registro_Medico
-- Medicamento
-- Formula_Medica
-- Causa
-- Causa_Cita
-- Campana_Prevencion
-- Campana_Paciente

--==================================>  CREAR LAS TABLAS <================================

CREATE TABLE Area
(
	codigo INTEGER NOT NULL PRIMARY KEY,
	nombre VARCHAR (100) NOT NULL,
	descripcion TEXT NOT NULL
);


CREATE TABLE Cama
(
	num_cama INTEGER NOT NULL PRIMARY KEY,
	estado BOOLEAN,
	descripcion TEXT NOT NULL,
	codigo_area INTEGER NOT NULL,

	CONSTRAINT area_fk FOREIGN KEY (codigo_area)
	REFERENCES Area (codigo)
	ON UPDATE CASCADE ON DELETE CASCADE
);


CREATE TABLE Persona
(
	identificacion INTEGER NOT NULL PRIMARY KEY,
	nombre VARCHAR(50) NOT NULL,
	direccion VARCHAR (100) NOT NULL,
	telefono VARCHAR(15) NOT NULL
);


CREATE TABLE Paciente
(
	identificacion INTEGER NOT NULL PRIMARY KEY,
	fecha_nacimiento DATE NOT NULL,
	actividad_economica VARCHAR(100) NOT NULL,
	num_seguridad_social INTEGER NOT NULL,

	CONSTRAINT persona_fk FOREIGN KEY (identificacion)
	REFERENCES Persona (identificacion)
	ON UPDATE CASCADE ON DELETE CASCADE 
);


CREATE TABLE Empleado
(
	identificacion INTEGER NOT NULL PRIMARY KEY,
	codigo_area INTEGER NOT NULL,
	email VARCHAR(50) NOT NULL,
	salario MONEY NOT NULL,
	id_jefe INTEGER NOT NULL,

	CONSTRAINT empleado_fk FOREIGN KEY (id_jefe)
	REFERENCES Empleado (identificacion)
	ON UPDATE CASCADE ON DELETE CASCADE, 

	CONSTRAINT persona_fk FOREIGN KEY (identificacion)
	REFERENCES Persona (identificacion)
	ON UPDATE CASCADE ON DELETE CASCADE
);


CREATE TABLE Medico
(
	identificacion INTEGER NOT NULL PRIMARY KEY,
	especialidad VARCHAR (100) NOT NULL,
	universidad VARCHAR (100) NOT NULL,
	num_licencia INTEGER NOT NULL,

	CONSTRAINT empleado_fk FOREIGN KEY (identificacion)
	REFERENCES Empleado (identificacion)
	ON UPDATE CASCADE ON DELETE CASCADE
);


CREATE TABLE Enfermera
(
	identificacion INTEGER NOT NULL PRIMARY KEY,
	anos_experiencia INTEGER NOT NULL,

	CONSTRAINT empleado_fk FOREIGN KEY (identificacion)
	REFERENCES Empleado (identificacion)
	ON UPDATE CASCADE ON DELETE CASCADE
);


CREATE TABLE Habilidad
(
	codigo INTEGER NOT NULL PRIMARY KEY,
	descripcion TEXT NOT NULL
);


CREATE TABLE Enfermera_Habilidad
(
	id_enfermera INTEGER NOT NULL,
	habilidad INTEGER NOT NULL,
	
	CONSTRAINT id_enfermera_pk PRIMARY KEY (id_enfermera, habilidad),

	CONSTRAINT id_enfermera_fk FOREIGN KEY (id_enfermera)
	REFERENCES Enfermera (identificacion)
	ON UPDATE CASCADE ON DELETE CASCADE,
	
	CONSTRAINT habilidad_fk FOREIGN KEY (habilidad)
	REFERENCES Habilidad (codigo)
	ON UPDATE CASCADE ON DELETE CASCADE
);


CREATE TABLE Cama_Paciente
(
	num_cama INTEGER NOT NULL,
	id_paciente INTEGER NOT NULL,
	fecha_asignacion TIMESTAMP NOT NULL,

	CONSTRAINT cama_paciente_pk PRIMARY KEY (num_cama, id_paciente, fecha_asignacion),

	CONSTRAINT cama_fk FOREIGN KEY (num_cama)
	REFERENCES Cama (num_cama)
	ON UPDATE CASCADE ON DELETE CASCADE,

	CONSTRAINT paciente_fk FOREIGN KEY (id_paciente)
	REFERENCES Paciente (identificacion)
	ON UPDATE CASCADE ON DELETE CASCADE
);


CREATE TABLE Historia_Clinica
(
	numero_historia INTEGER NOT NULL PRIMARY KEY,
	id_paciente INTEGER NOT NULL,
	fecha_apertura DATE NOT NULL,

	CONSTRAINT paciente_fk FOREIGN KEY (id_paciente)
	REFERENCES Paciente (identificacion)
	ON UPDATE CASCADE ON DELETE CASCADE
);


CREATE TABLE Horario_Consulta
(
	id_horario INTEGER NOT NULL,
	id_medico INTEGER NOT NULL,
	fecha_hora TIMESTAMP NOT NULL,
	disponible BOOLEAN DEFAULT TRUE,

	CONSTRAINT horario_pk PRIMARY KEY (id_horario),

	CONSTRAINT medico_fk FOREIGN KEY (id_medico)
	REFERENCES Medico (identificacion)
	ON UPDATE CASCADE ON DELETE CASCADE
);


CREATE TABLE Cita
(
	id_horario INTEGER NOT NULL,
	numero_historia INTEGER NOT NULL,
	asistencia BOOLEAN DEFAULT FALSE,
	tipo_solicitud VARCHAR(50) NOT NULL,

	CONSTRAINT cita_pk PRIMARY KEY (id_horario, numero_historia),

	CONSTRAINT horario_fk FOREIGN KEY (id_horario)
	REFERENCES Horario_Consulta (id_horario)
	ON UPDATE CASCADE ON DELETE CASCADE,

	CONSTRAINT historia_fk FOREIGN KEY (numero_historia)
	REFERENCES Historia_Clinica (numero_historia)
	ON UPDATE CASCADE ON DELETE CASCADE
);


CREATE TABLE Registro_Medico
(
	numero_registro INTEGER NOT NULL PRIMARY KEY,
	id_horario INTEGER NOT NULL,
	numero_historia INTEGER NOT NULL,
	costo MONEY NOT NULL,


	CONSTRAINT horario_fk FOREIGN KEY (id_horario)
	REFERENCES Horario_Consulta (id_horario)
	ON UPDATE CASCADE ON DELETE CASCADE,

	CONSTRAINT historia_fk FOREIGN KEY (numero_historia)
	REFERENCES Historia_Clinica (numero_historia)
	ON UPDATE CASCADE ON DELETE CASCADE
);


CREATE TABLE Medicamento
(
	codigo INTEGER NOT NULL PRIMARY KEY,
	costo MONEY NOT NULL,
	nombre VARCHAR (50) NOT NULL,
	descripcion TEXT
);


CREATE TABLE Formula_Medica
(
	numero_registro INTEGER NOT NULL,
	codigo_medicamento INTEGER NOT NULL,
	cantidad INTEGER NOT NULL,

	CONSTRAINT formula_medica_pk PRIMARY KEY (numero_registro, codigo_medicamento),

	CONSTRAINT registro_medico_fk FOREIGN KEY(numero_registro)
	REFERENCES Registro_Medico (numero_registro)
	ON UPDATE CASCADE ON DELETE CASCADE,

	CONSTRAINT medicamento_fk FOREIGN KEY(codigo_medicamento)
	REFERENCES Medicamento (codigo)
	ON UPDATE CASCADE ON DELETE CASCADE
);


CREATE TABLE Causa
(
	codigo INTEGER NOT NULL PRIMARY KEY,
	nombre VARCHAR (50) NOT NULL,
	descripcion TEXT NOT NULL
);


CREATE TABLE Causa_Cita
(
	numero_registro INTEGER NOT NULL,
	id_causa INTEGER NOT NULL,

	CONSTRAINT causa_cita_pk PRIMARY KEY (numero_registro, id_causa),

	CONSTRAINT registro_medico_fk FOREIGN KEY(numero_registro)
	REFERENCES Registro_Medico (numero_registro)
	ON UPDATE CASCADE ON DELETE CASCADE,

	CONSTRAINT causa_fk FOREIGN KEY(id_causa)
	REFERENCES Causa (codigo)
	ON UPDATE CASCADE ON DELETE CASCADE
);


CREATE TABLE Campana_Prevencion
(
	codigo VARCHAR (20) NOT NULL PRIMARY KEY,
	id_medico INTEGER NOT NULL,
	nombre VARCHAR (100) NOT NULL,
	fecha_realizacion DATE NOT NULL,
	objetivo TEXT,

	CONSTRAINT medico_fk FOREIGN KEY (id_medico)
	REFERENCES Medico (identificacion)
	ON UPDATE CASCADE ON DELETE CASCADE
);


CREATE TABLE Campana_Paciente
(
	id_paciente INTEGER NOT NULL,
	codigo_campana VARCHAR (20),

	CONSTRAINT campana_paciente_pk PRIMARY KEY (id_paciente, codigo_campana),

	CONSTRAINT paciente_fk FOREIGN KEY (id_paciente)
	REFERENCES Paciente (identificacion)
	ON UPDATE CASCADE ON DELETE CASCADE,

	CONSTRAINT campana_fk FOREIGN KEY (codigo_campana)
	REFERENCES Campana_Prevencion (codigo)
	ON UPDATE CASCADE ON DELETE CASCADE
);

--=========================> CREACION DE RESTRICCIONES (UNIQUE) <========================
ALTER TABLE Horario_Consulta
ADD CONSTRAINT uniq_medico_fecha
UNIQUE (id_medico, fecha_hora);

--NUEVOS UNIQUE
ALTER TABLE Area
ADD CONSTRAINT uniq_area_nombre
UNIQUE (codigo, nombre);

ALTER TABLE Habilidad
ADD CONSTRAINT uniq_habilidad_descripcion
UNIQUE (codigo, descripcion);

ALTER TABLE Causa
ADD CONSTRAINT uniq_causa_nombre
UNIQUE (codigo, nombre);

ALTER TABLE Medicamento
ADD CONSTRAINT uniq_medicamento_nombre
UNIQUE (nombre);
--=======================================================================================


-- CREACION DE SECUENCIAS (SEQUENCE):


--====================> CREACION Y ASIGNACION DE SECUENCIA (SEQUENCE)==================

CREATE SEQUENCE seq_cod_area START 1;
CREATE SEQUENCE seq_num_cama START 1;
CREATE SEQUENCE seq_cod_habilidad START 1;
CREATE SEQUENCE seq_num_historia START 1;
CREATE SEQUENCE seq_id_horario START 1;
CREATE SEQUENCE seq_num_registro START 1;
CREATE SEQUENCE seq_cod_causa START 1;
--NUEVA SECUENCIA
CREATE SEQUENCE seq_cod_medicamento START 1;

-- ASIGNACION DE SECUENCIAS (SEQUENCE):
ALTER TABLE Area ALTER COLUMN codigo
SET DEFAULT nextval('seq_cod_area');

ALTER TABLE Cama ALTER COLUMN num_cama
SET DEFAULT nextval('seq_num_cama');

ALTER TABLE Habilidad ALTER COLUMN codigo
SET DEFAULT nextval('seq_cod_habilidad');

ALTER TABLE Historia_Clinica ALTER COLUMN numero_historia
SET DEFAULT nextval('seq_num_historia');

ALTER TABLE Horario_Consulta ALTER COLUMN id_horario
SET DEFAULT nextval('seq_id_horario');

ALTER TABLE Registro_Medico ALTER COLUMN numero_registro
SET DEFAULT nextval('seq_num_registro');

ALTER TABLE Causa ALTER COLUMN codigo
SET DEFAULT nextval('seq_cod_causa');

--NUEVA SECUENCIA
ALTER TABLE Medicamento ALTER COLUMN codigo
SET DEFAULT nextval('seq_cod_medicamento');
--=======================================================================================


ALTER TABLE Empleado
  ADD CONSTRAINT empleado_codigo_area_fk
  FOREIGN KEY (codigo_area)
  references Area (codigo);


--==============================> CREACION DE TRIGGERS <=================================

-- trigger Asociar_Historia
CREATE FUNCTION Asociar_Historia() RETURNS trigger AS $asociar_historia$
    BEGIN
        INSERT INTO Historia_clinica (id_paciente, fecha_apertura) 
        VALUES (NEW.identificacion, now());
        RETURN NULL;
    END;
$asociar_historia$ LANGUAGE plpgsql;

CREATE TRIGGER asociar_historia AFTER INSERT ON Paciente
    FOR EACH ROW EXECUTE PROCEDURE Asociar_Historia();

-- trigger 
--=======================================================================================




