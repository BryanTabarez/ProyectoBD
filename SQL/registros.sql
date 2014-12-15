--=======================================================================================
--========================== BASE DE DATOS PARA PRUEBAS =================================
--=======================================================================================

-- INSERTAR AREAS DEL HOSPITAL: Area (codigo, nombre, descripcion)
INSERT INTO Area(nombre, descripcion) VALUES ('Urgencias', 'Atencion integral del paciente que requiere atencion medica de emergencia.');
INSERT INTO Area(nombre, descripcion) VALUES ('Pediatria', 'Cirugias ambulatorias y Hospitalizacion desde Recien Nacido hasta menores de 16 años.');
INSERT INTO Area(nombre, descripcion) VALUES ('Ginecologia', 'Consulta de Ginecología General | Consulta de Ginecología Oncológica | Consulta de Ginecología Urológica | Consulta de Menopausia');
INSERT INTO Area(nombre, descripcion) VALUES ('Cirujia', 'El Departamento de Cirugía es el órgano de línea final, que se encarga de prestar atención médica integral a los pacientes con enfermedades médico-quirúrgicas mediante acciones de promoción, prevención, recuperación y rehabilitación en forma individual y colectiva.')

-- INSERTAR CAMAS: Cama (num_cama, estado, descripcion, codigo_area)
INSERT INTO Cama(estado, descripcion, codigo_area) VALUES (TRUE, 'una cama es una cama ._.', 1);
INSERT INTO Cama(estado, descripcion, codigo_area) VALUES (TRUE, 'esta es una descripcion...', 4);

-- INSERTAR PERSONAS: Persona (identificacion, nombre, direccion, telefono)
INSERT INTO Persona VALUES (1111, 'Carlos Wasowsky', 'Calle 5', '3216406464');
INSERT INTO Persona VALUES (2222, 'Ardila Lule', 'Calle 6 oeste', '3054238585');

--INSERTAR PACIENTE: Paciente (identificacion, fecha_nacimiento, actividad_economica, num_seguridad_social)
INSERT INTO Paciente VALUES (2222, '1950-1-1', 'super empresario dueño de medio colombia', 2222);
-- INSERTAR EMPLEADOS: Empleado (identificacion, codigo_area, email, salario, id_jefe)
INSERT INTO Empleado VALUES (1111, 1, 'carlos@wasowsky.com', 3500000, 1111);
-- INSERTAR MEDICOS: Medico (identificacion, especialidad, universidad, num_licencia)
INSERT INTO Medico VALUES (1111, 'Especialidad en Urgencias Medicas', 'Javeriana', 7777);

INSERT INTO Persona VALUES (110, 'Antonio', 'CALLE 13 CRA 5', '4444123');
INSERT INTO Empleado VALUES (110,  1, 'antonio@correo.com', 2500000, 110);

INSERT INTO Habilidad (descripcion) VALUES ('cuidar viejitos');
INSERT INTO Habilidad (descripcion) VALUES ('inyectar'); 

-- George lo hizo

--INSERTAR HORARIO CONSULTA: Horario_Consulta (id_horario, id_medico, fecha_hora, disponible)
INSERT INTO Horario_Consulta (id_medico, fecha_hora, disponible) VALUES (1111, '2014-1-1 02:30:10', 'true');

--INSERTAR Cita: Cita(id_horario, id_paciente, asistencia, tipo_solicitud)
INSERT INTO Cita VALUES (1, 2222, 'true', 'dolencia en el cuerpo');

--INSERTAR Registro Medico: Registro_Medico(numero_registro, id_horario, id_paciente, costo)
INSERT INTO Registro_Medico ( id_horario, id_paciente, costo) VALUES (1, 2222, '25000');

--INSERTAR Medicamento: Medicamento (codigo,  costo, nombre, descripcion)  
INSERT INTO Medicamento (costo, nombre, descripcion) VALUES ('1000', 'Acetaminofen 500mg', 'es de uso general para cualquier sintoma');

-- Acetaminofeno (Rectal)
-- se usa para aliviar el dolor y reducir la fiebre. A diferencia de la aspirina, no alivia el enrojecimiento, la rigidez o la hinchazon causados por la artritis reumatoidea. Sin embargo, puede aliviar el dolor causado por formas leves de artritis. 

-- Albendazol (Oral)
-- se usa para tratar las infecciones por lombrices causadas por ascarides, anquilostomas, oxiuros, tenias y nematodos comunes. Tambien se usa para tratar infecciones por lombrices llamadas estrongiloidiasis y la enfermedad hidatidica (tenias de perro que pueden infectar a los seres humanos). 
