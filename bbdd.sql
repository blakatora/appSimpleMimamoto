-- Crear tabla cliente
CREATE TABLE cliente (
    id SERIAL PRIMARY KEY,
    nombre_completo VARCHAR(100) NOT NULL,
    correo VARCHAR(100),
    telefono VARCHAR(20) NOT NULL,
    direccion VARCHAR(255),
    dni VARCHAR(20) UNIQUE 
);

-- Crear tabla moto
CREATE TABLE moto (
    id SERIAL PRIMARY KEY,
    marca VARCHAR(50),
    modelo VARCHAR(50),
    año INTEGER,
    matricula VARCHAR(20) NOT NULL,
    propietario INTEGER REFERENCES cliente(id)
);

-- Crear tabla reparacion
CREATE TABLE reparacion (
    id SERIAL PRIMARY KEY,
    descripcion TEXT,
    fecha DATE,
    moto_id INTEGER REFERENCES moto(id),
    cliente_id INTEGER REFERENCES cliente(id),
    precio_total NUMERIC(10, 2),
    kilometros INTEGER
);

insert c
select * from moto;

INSERT INTO moto (marca, modelo, año, matricula, propietario)
VALUES ('Yamaha', 'MT-07', 2022, '5678-DEF', 1);

select * from moto where propietario= 1;

SELECT moto.id,moto.marca,moto.modelo,moto.año,moto.matricula,cliente.nombre_completo
FROM moto 
inner join cliente on cliente.id=moto.propietario
where moto.propietario = 1;

SELECT moto.id,moto.marca,moto.modelo,moto.año,moto.matricula,cliente.nombre_completo
FROM moto 
inner join cliente on cliente.id=moto.propietario
where moto.propietario = {cliente};

select id from moto;
