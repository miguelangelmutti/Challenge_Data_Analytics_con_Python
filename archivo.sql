CREATE TABLE public.espacios_culturales_2 (
    id integer NOT NULL, 
    cod_localidad integer, 
    id_provincia integer, 
    id_departamento integer, 
    categoria character varying(200) NOT NULL, 
    provincia character varying(200), 
    localidad character varying(200), 
    nombre character varying(200) NOT NULL, 
    domicilio character varying(200), 
    cp character varying(200), 
    telefono character varying(200), 
    mail character varying(200), 
    web character varying(200), 
    creado timestamp without time zone
);