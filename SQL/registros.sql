--=======================================================================================
--========================== BASE DE DATOS PARA PRUEBAS =================================
--=======================================================================================

-- INSERTAR AREAS DEL HOSPITAL: Area (codigo, nombre, descripcion)
INSERT INTO Area(nombre, descripcion) VALUES ('Urgencias', 'Atención integral del paciente que requiere atención médica de emergencia.');
INSERT INTO Area(nombre, descripcion) VALUES ('Pediatria', 'Cirugías ambulatorias y Hospitalización desde Recién Nacido hasta menores de 16 años.');
INSERT INTO Area(nombre, descripcion) VALUES ('Ginecologia', 'Consulta de Ginecología General | Consulta de Ginecología Oncológica | Consulta de Ginecología Urológica | Consulta de Menopausia');
INSERT INTO Area(nombre, descripcion) VALUES ('Cirujia', 'El Departamento de Cirugía es el órgano de línea final, que se encarga de prestar atención médica integral a los pacientes con enfermedades médico-quirúrgicas mediante acciones de promoción, prevención, recuperación y rehabilitación en forma individual y colectiva.')

-- INSERTAR CAMAS: Cama (num_cama, estado, descripcion, codigo_area)
INSERT INTO Cama(estado, descripcion, codigo_area) VALUES (TRUE, 'una cama es una cama ._.', 1);
INSERT INTO Cama(estado, descripcion, codigo_area) VALUES (TRUE, 'esta es una descripcion...', 4);

-- INSERTAR PERSONAS: Persona (identificacion, nombre, direccion, telefono)
INSERT INTO Persona VALUES (1111, 'Carlos Wasowsky', 'Calle 5', '3216406464');
-- INSERTAR EMPLEADOS: Empleado (identificacion, codigo_area, email, salario, id_jefe)
INSERT INTO Empleado VALUES (1111, 1, 'carlos@wasowsky.com', 3500000, 1111);
-- INSERTAR MEDICOS: Medico (identificacion, especialidad, universidad, num_licencia)
INSERT INTO Medico VALUES (1111, 'Especialidad en Urgencias Medicas', 'Javeriana', 7777);

INSERT INTO Persona VALUES (110, 'Antonio', 'CALLE 13 CRA 5', '4444123');
INSERT INTO Empleado VALUES (110,  1, 'antonio@correo.com', 2500000, 110);

INSERT INTO Habilidad (descripcion) VALUES ('cuidar viejitos');
INSERT INTO Habilidad (descripcion) VALUES ('inyectar');
