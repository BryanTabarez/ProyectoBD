--=======================================================================================
--
-- INTEGRANTES:
-- Bryan Stiven Tabarez Mestra	- 1131782
-- Aurelio Antonio Vivas Meza	- 1110348
-- George Romero Ramirez		- 1130924
--
--=======================================================================================

--=================>  CREAR LAS TABLAS <=================

CREATE TABLE Area
(
	codigo INTEGER NOT NULL PRIMARY KEY,
	nombre VARCHAR (100) NOT NULL,
	descripcion TEXT NOT NULL
);


CREATE TABLE Cama
(
	num_cama INTEGER NOT NULL PRIMARY KEY,
	estado VARCHAR (20) NOT NULL,
	descripcion TEXT NOT NULL,
	codigo_area INTEGER NOT NULL,

	CONSTRAINT area_fk FOREIGN KEY (codigo_area)
	REFERENCES Area (codigo)
	ON UPDATE CASCADE ON DELETE NO ACTION
);


CREATE TABLE Persona
(
	identificacion INTEGER NOT NULL PRIMARY KEY,
	nombre VARCHAR(50) NOT NULL,
	direccion VARCHAR (100) NOT NULL,
	telefono INTEGER NOT NULL
);


CREATE TABLE Paciente
(
	identificacion INTEGER NOT NULL PRIMARY KEY,
	fecha_nacimiento DATE NOT NULL,
	actividad_economica VARCHAR(100) NOT NULL,
	num_seguridad_social INTEGER NOT NULL,

	CONSTRAINT persona_fk FOREIGN KEY (identificacion)
	REFERENCES Persona (identificacion)
	ON UPDATE CASCADE ON DELETE NO ACTION 
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
	ON UPDATE CASCADE ON DELETE NO ACTION, 

	CONSTRAINT persona_fk FOREIGN KEY (identificacion)
	REFERENCES Persona (identificacion)
	ON UPDATE CASCADE ON DELETE NO ACTION 
);


CREATE TABLE Medico
(
	identificacion INTEGER NOT NULL PRIMARY KEY,
	especialidad VARCHAR (100) NOT NULL,
	universidad VARCHAR (100) NOT NULL,
	num_licencia INTEGER NOT NULL,

	CONSTRAINT empleado_fk FOREIGN KEY (identificacion)
	REFERENCES Empleado (identificacion)
	ON UPDATE CASCADE ON DELETE NO ACTION
);


CREATE TABLE Enfermera
(
	identificacion INTEGER NOT NULL PRIMARY KEY,
	anos_experiencia INTEGER NOT NULL,

	CONSTRAINT empleado_fk FOREIGN KEY (identificacion)
	REFERENCES Empleado (identificacion)
	ON UPDATE CASCADE ON DELETE NO ACTION
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
	
	CONSTRAINT id_enfermera_pk PRIMARY KEY (id_enfermera),

	CONSTRAINT id_enfermera_fk FOREIGN KEY (id_enfermera)
	REFERENCES Enfermera (identificacion)
	ON UPDATE CASCADE ON DELETE NO ACTION,
	
	CONSTRAINT habilidad_fk FOREIGN KEY (habilidad)
	REFERENCES Habilidad (codigo)
	ON UPDATE CASCADE ON DELETE NO ACTION
);


CREATE TABLE Cama_Paciente
(
	num_cama INTEGER NOT NULL,
	id_paciente INTEGER NOT NULL,
	fecha_asignacion TIMESTAMP NOT NULL,

	CONSTRAINT cama_paciente_pk PRIMARY KEY (num_cama, id_paciente, fecha_asignacion),

	CONSTRAINT cama_fk FOREIGN KEY (num_cama)
	REFERENCES Cama (num_cama)
	ON UPDATE CASCADE ON DELETE NO ACTION,

	CONSTRAINT paciente_fk FOREIGN KEY (id_paciente)
	REFERENCES Paciente (identificacion)
	ON UPDATE CASCADE ON DELETE NO ACTION
);


CREATE TABLE Historia_Clinica
(
	numero_historia INTEGER NOT NULL PRIMARY KEY,
	id_paciente INTEGER NOT NULL,
	fecha_apertura DATE NOT NULL,

	CONSTRAINT paciente_fk FOREIGN KEY (id_paciente)
	REFERENCES Paciente (identificacion)
	ON UPDATE CASCADE ON DELETE NO ACTION
);


CREATE TABLE Horario_Consulta
(
	id_horario INTEGER NOT NULL,
	id_medico INTEGER NOT NULL,
	fecha_hora TIMESTAMP NOT NULL,
	vacante BOOLEAN DEFAULT TRUE,

	CONSTRAINT horario_pk PRIMARY KEY (id_horario),

	CONSTRAINT medico_fk FOREIGN KEY (id_medico)
	REFERENCES Medico (identificacion)
	ON UPDATE CASCADE ON DELETE NO ACTION
);


CREATE TABLE Cita
(
	id_horario INTEGER NOT NULL,
	numero_historia INTEGER NOT NULL,
	asistencia BOOLEAN DEFAULT FALSE,
	tipo_solicitud VARCHAR(20) NOT NULL,

	CONSTRAINT cita_pk PRIMARY KEY (id_horario, numero_historia),

	CONSTRAINT horario_fk FOREIGN KEY (id_horario)
	REFERENCES Horario_Consulta (id_horario)
	ON UPDATE CASCADE ON DELETE NO ACTION,

	CONSTRAINT historia_fk FOREIGN KEY (numero_historia)
	REFERENCES Historia_Clinica (numero_historia)
	ON UPDATE CASCADE ON DELETE NO ACTION
);


CREATE TABLE Registro_Medico
(
	numero_registro INTEGER NOT NULL PRIMARY KEY,
	id_horario INTEGER NOT NULL,
	numero_historia INTEGER NOT NULL,
	costo MONEY NOT NULL,


	CONSTRAINT horario_fk FOREIGN KEY (id_horario)
	REFERENCES Horario_Consulta (id_horario)
	ON UPDATE CASCADE ON DELETE NO ACTION,

	CONSTRAINT historia_fk FOREIGN KEY (numero_historia)
	REFERENCES Historia_Clinica (numero_historia)
	ON UPDATE CASCADE ON DELETE NO ACTION
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
	ON UPDATE CASCADE ON DELETE NO ACTION,

	CONSTRAINT medicamento_fk FOREIGN KEY(codigo_medicamento)
	REFERENCES Medicamento (codigo)
	ON UPDATE CASCADE ON DELETE NO ACTION
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
	ON UPDATE CASCADE ON DELETE NO ACTION,

	CONSTRAINT causa_fk FOREIGN KEY(id_causa)
	REFERENCES Causa (codigo)
	ON UPDATE CASCADE ON DELETE NO ACTION
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
	ON UPDATE CASCADE ON DELETE NO ACTION
);


CREATE TABLE Campana_Paciente
(
	id_paciente INTEGER NOT NULL,
	codigo_campana VARCHAR (20),

	CONSTRAINT campana_paciente_pk PRIMARY KEY (id_paciente, codigo_campana),

	CONSTRAINT paciente_fk FOREIGN KEY (id_paciente)
	REFERENCES Paciente (identificacion)
	ON UPDATE CASCADE ON DELETE NO ACTION,

	CONSTRAINT campana_fk FOREIGN KEY (codigo_campana)
	REFERENCES Campana_Prevencion (codigo)
	ON UPDATE CASCADE ON DELETE NO ACTION
);


CREATE UNIQUE INDEX horario_restriccion ON Horario_Consulta (id_medico, fecha_hora);







