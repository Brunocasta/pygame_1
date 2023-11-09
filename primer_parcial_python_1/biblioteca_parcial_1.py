import json
import re 
import csv
import sqlite3

class Estadisticas:
    def __init__(self,temporadas = 0,puntos_totales = 0,promedio_puntos_por_partido = 0,rebotes_totales = 0,promedio_rebotes_por_partido= 0,asistencias_totales= 0,
                promedio_asistencias_por_partido = 0,robos_totales = 0.0,bloqueos_totales = 0.0, porcentaje_tiros_campo = 0 ,porcentaje_tiros_libres = 0 ,porcentaje_tiros_triples = 0):
        self._temporadas = temporadas
        self._puntos_totales = puntos_totales
        self._promedio_puntos_por_partido = promedio_puntos_por_partido
        self._rebotes_totales = rebotes_totales
        self._promedio_rebotes_por_partido = promedio_rebotes_por_partido
        self._asistencias_totales = asistencias_totales
        self._promedio_asistencias_por_partido = promedio_asistencias_por_partido
        self._robos_totales = robos_totales
        self._bloqueos_totales = bloqueos_totales
        self._porcentaje_tiros_campo = porcentaje_tiros_campo
        self._porcentaje_tiros_libres = porcentaje_tiros_libres
        self._porcentaje_tiros_triples = porcentaje_tiros_triples
        
    # Getters
    @property
    def temporadas(self):
        return self._temporadas
    
    @property
    def puntos_totales(self):
        return self._puntos_totales
        
    @property
    def promedio_puntos_por_partido(self):
        return self._promedio_puntos_por_partido
        
    @property
    def rebotes_totales(self):
        return self._rebotes_totales
    
    @property
    def promedio_rebotes_por_partido(self):
        return self._promedio_rebotes_por_partido
        
    @property
    def asistencias_totales(self):
        return self._asistencias_totales
        
    @property
    def promedio_asistencias_por_partido(self):
        return self._promedio_asistencias_por_partido
    
    @property
    def robos_totales(self):
        return self._robos_totales
        
    @property
    def bloqueos_totales(self):
        return self._bloqueos_totales
        
    @property
    def porcentaje_tiros_campo(self):
        return self._porcentaje_tiros_campo
    
    @property
    def porcentaje_tiros_libres(self):
        return self._porcentaje_tiros_libres
        
    @property
    def porcentaje_tiros_triples(self):
        return self._porcentaje_tiros_triples
        
    # Setters
    @temporadas.setter
    def temporadas(self, value):
        self._temporadas = value

    @puntos_totales.setter
    def puntos_totales(self, value):
        self._puntos_totales = value

    @promedio_puntos_por_partido.setter
    def promedio_puntos_por_partido(self, value):
        self._promedio_puntos_por_partido = value

    @rebotes_totales.setter
    def rebotes_totales(self, value):
        self._rebotes_totales = value

    @promedio_rebotes_por_partido.setter
    def promedio_rebotes_por_partido(self, value):
        self._promedio_rebotes_por_partido = value

    @asistencias_totales.setter
    def asistencias_totales(self, value):
        self._asistencias_totales = value

    @promedio_asistencias_por_partido.setter
    def promedio_asistencias_por_partido(self, value):
        self._promedio_asistencias_por_partido = value

    @robos_totales.setter
    def robos_totales(self, value):
        self._robos_totales = value

    @bloqueos_totales.setter
    def bloqueos_totales(self, value):
        self._bloqueos_totales = value

    @porcentaje_tiros_campo.setter
    def porcentaje_tiros_campo(self, value):
        self._porcentaje_tiros_campo = value

    @porcentaje_tiros_libres.setter
    def porcentaje_tiros_libres(self, value):
        self._porcentaje_tiros_libres = value

    @porcentaje_tiros_triples.setter
    def porcentaje_tiros_triples(self, value):
        self._porcentaje_tiros_triples = value

class Jugador:
    def __init__(self,nombre,posicion,logros,estadisticas):
        self._nombre = nombre
        self._posicion = posicion
        self._estadisticas = estadisticas
        self._logros = logros 
        
    # Getters
    @property
    def nombre(self):
        return self._nombre

    @property
    def posicion(self):
        return self._posicion
        
    @property
    def estadisticas(self):
        return self._estadisticas
        
    @property
    def logros(self):
        return self._logros

    # Setters
    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @posicion.setter
    def posicion(self, value):
        self._posicion = value

    @estadisticas.setter
    def estadisticas(self, value):
        self._estadisticas = value
        
    @logros.setter
    def logros(self, value):
        self._logros = value
    
class Equipo:
    def __init__(self,json_file):
        self._jugadores_team = []
        self.load_players_from_json(json_file)  
        
        
    # Getter para obtener la lista de jugadores
    @property
    def jugadores_team(self):
        return self._jugadores_team

    # Setter para modificar la lista de jugadores
    @jugadores_team.setter
    def jugadores_team(self, value):
        self._jugadores_team = value
    
    def load_players_from_json(self,json_file):
        """ Esta funcion se encarga de cargar el archivo en modo lectura parapoder pasar los valores a cada una de las clases
            a cual les corresponda

        Args:
            json_file (_type_): recibe como parametro una variable que va a tomar el valor del path de el archivo json 
            para luego poder usarlo 
        """
        try:
            with open(json_file, 'r',encoding='UTF-8') as file:
                data = json.load(file)["jugadores"]
                for info_jugador in data:
                    info_estadisticas = info_jugador["estadisticas"]
                    estadisticas = Estadisticas(
                            info_estadisticas["temporadas"],
                            info_estadisticas["puntos_totales"],
                            info_estadisticas["promedio_puntos_por_partido"],
                            info_estadisticas["rebotes_totales"],
                            info_estadisticas["promedio_rebotes_por_partido"],
                            info_estadisticas["asistencias_totales"],
                            info_estadisticas["promedio_asistencias_por_partido"],
                            info_estadisticas["robos_totales"],
                            info_estadisticas["bloqueos_totales"],
                            info_estadisticas["porcentaje_tiros_de_campo"],
                            info_estadisticas["porcentaje_tiros_libres"],
                            info_estadisticas["porcentaje_tiros_triples"],
                        )
                    jugador = Jugador(info_jugador["nombre"],info_jugador["posicion"],info_jugador["logros"],estadisticas)
                    self.jugadores_team.append(jugador)
        except Exception as e:
            print(f"Error al cargar los jugadores desde el archivo JSON: {str(e)}")

    def obtener_nombre_y_dato(self):
        """Esta funcion se encarga de recorrer el listado de jugadores y muestra el nombre y 
            la posicion de cada uno ,junto con su indice 
        """
        i=0
        for jugador in self.jugadores_team:
            print(f"{i} - {jugador.nombre} - {jugador.posicion}")
            i += 1

    def obtener_indice_jugador (self):
        """Esta funcion va pedir al usuario que ingrese un undice del jugador que se muestra en pantalla 
            ,el cual si es correcto es retornado para poder realizar lo que se pida
            en caso contrario ,retornara un mensaje indicando que es oncorrecto lo que ingreso

        Returns:
            _type_: retorna un numero que es el indice que se pidio por consola
        """
        indice_jugador= int(input("Indique indice de jugador: "))
        if indice_jugador > len(self.jugadores_team) - 1 and indice_jugador < 0 :
            return print("Error...No es un indice correcto ")
        else:
            return indice_jugador
    
    def estadisticas_jugadores(self,indice):
        """Esta funcion recibe como parametro un indice ,que va ser el que se pase a la lista de los jugadores ,para que luego 
        se le adjudique a una variable ,que toma los datos de el jugador elegido 
        que tambien debera mostrar todas las estadisticas ,tal cual lo idica el nombre de la funcion 

        Args:
            indice (): se recibe como parametro para indicar cual es el jugador que se pide mostrar las estadisticas junto con su nombre
        """
        jugador  = self.jugadores_team[indice]
        estadistica_jugador = jugador.estadisticas
        print(f"***Nombre jugador Seleccionado: {jugador.nombre} ")
        print(f"\nTemporadas: {estadistica_jugador.temporadas} ")
        print(f"Puntos Totales: {estadistica_jugador.puntos_totales} ")
        print(f"Promedio de puntos por partido: {estadistica_jugador.promedio_puntos_por_partido} ")
        print(f"Rebotes totales: {estadistica_jugador.rebotes_totales} ")
        print(f"Rebotes promedio por partido: {estadistica_jugador.promedio_rebotes_por_partido} ")
        print(f"Asistencias totales: {estadistica_jugador.asistencias_totales} ")
        print(f"Promedio de asistencias por partido: {estadistica_jugador.promedio_asistencias_por_partido} ")
        print(f"Robos totales: {estadistica_jugador.robos_totales} ")
        print(f"Bloqueos totales: {estadistica_jugador.bloqueos_totales} ")
        print(f"Porcentaje tiros de campo: {estadistica_jugador.porcentaje_tiros_campo} ")
        print(f"Procentaje de tiros libres: {estadistica_jugador.porcentaje_tiros_libres} ")
        print(f"Porcentajes de tiros triples: {estadistica_jugador.porcentaje_tiros_triples} ")

    def guardar_estadisticas_archivo_csv(self, indice):
        """Esta funcion toma el indice que se recibe por parametro ,para luego asignarsela a la lista de jugadores y tomar al jugador que elige el usuario 
        y poder asi guardar en un archivo CSV los datos que se necesitan guardar ,en el archivo. El cual va a tomar el nombre de el jugador que se eligio

        Args:
            indice (_type_): se recibe como parametro para indicar cual es el jugador que se pide mostrar las estadisticas junto con su nombre

        Returns:
            _type_: La funcion retorna True junto con un mensaje de que fue cargado con exito el archio o 
                    False mostrando que hubo una falla en la carga del archivo
        """
        jugador  = self.jugadores_team[indice]
        estadisticas_jugador = jugador.estadisticas
        try:
            with open(f"estadisticas_jugador_{jugador.nombre}.csv", mode="w",encoding='UTF-8',newline='') as archivo_guardar:
                escribir_archivo = csv.writer(archivo_guardar)

                escribir_archivo.writerow(["Nombre", "Posicion", "Temporadas", "Puntos totales","Promedio de puntos por partido","Rebotes totales",
                "Promedio de rebotes por partido","Asistencias totales", "promedio de asistencias por partido","Bloqueos totales","Porcentaje de tiros de campo",
                "Porcentaje de tiros libres","Porcentaje de tiros triples"])

                escribir_archivo.writerow([
                    jugador.nombre,jugador.posicion,estadisticas_jugador.temporadas,estadisticas_jugador.puntos_totales,estadisticas_jugador.promedio_puntos_por_partido,
                    estadisticas_jugador.rebotes_totales,estadisticas_jugador.promedio_rebotes_por_partido,estadisticas_jugador.asistencias_totales,estadisticas_jugador.promedio_asistencias_por_partido,
                    estadisticas_jugador.robos_totales,estadisticas_jugador.bloqueos_totales,estadisticas_jugador.porcentaje_tiros_campo,estadisticas_jugador.porcentaje_tiros_libres,
                    estadisticas_jugador.porcentaje_tiros_triples 
                    ])
                print(f"Se creó el archivo: estadisticas_jugador_{jugador.nombre}.csv")
            return True
        except Exception:
            print(f"Error al crear el archivo: estadisticas_jugador_{jugador.nombre}.csv")
            return False

    def buscar_jugador_nombre(self,nombre_jugador):
        """Esta funcion se encarga de buscar el nombre que se pasa por parametro con la variable de nombre_jugador para luego 
            hacer un search de nombre pasado por el usuarioo ,junto con algun nombre del jugador del listado 
            Si hay si hay match entre el nombre a buscar y uno de la lista , se mostrara los logros de ese jugador encontrado
        Args:
            nombre_jugador (_type_): recibe un string que en este caso es el nombre perteneciente a un jugador de la lista

        Returns:
            _type_: retornara el listado de los logros del jugador si sale todo ok 
            sino devolvera un e¿mensaje de que el jugador no coincide con los que esta en la lista
        """
        for jugador in self.jugadores_team:
            match_nombre = re.search(nombre_jugador,jugador.nombre,re.IGNORECASE)
            if jugador != None and match_nombre :
                print(f"\n *** {jugador.nombre} *** \n")
                for logros in jugador.logros:
                    print(f" {logros}")
        return print("No se encontro el jugador ingresado ")

    def calcular_promedio_puntos_por_partido(self):
        """ esta funcion se encarga de generar un acumulador de los promedios por partido de los jugadores del listado para poder saar un promedio del mismo 
            devolviendo el promedio del team como resultado
        """
        acumulador_estadisticas = 0
        for jugador in self.jugadores_team:
            acumulador_estadisticas += jugador.estadisticas.promedio_puntos_por_partido 
        promedio = acumulador_estadisticas/len(self.jugadores_team)
        promedio = round(promedio, 2)
        print(f"Promedio del Dream Team es: {promedio} \n")

    def jugadores_x_nombre(self):
        """Esta funcion se encarga de recorrer el listado de jugadores ,generando una nueva lista por sus nombres guardando los nombre y el promedio por puntos 
        """
        lista_a_ordenar = []
        for  jugador_ordenado in self.jugadores_team:
            lista_desordenada = f"{jugador_ordenado.nombre} - Promedio de puntos: {jugador_ordenado.estadisticas.promedio_puntos_por_partido}"
            lista_a_ordenar.append(lista_desordenada)
        return lista_a_ordenar
    
    def buscar_jugador_en_salon_fama(self,nombre_jugador):
        """Esta funcion se encarga de buscar el nombre que se pasa por parametro con la variable de nombre_jugador para luego 
            hacer un search de nombre pasado por el usuarioo ,junto con algun nombre del jugador del listado
            Si este jugador tiene dentro de sus logros ,ser miembro del salon de la fama del baloncesto ,imprimira si pertenece o no 

        Args:
            nombre_jugador (_type_): recibe un string que en este caso es el nombre perteneciente a un jugador de la lista

        Returns:
            _type_: Muestra el mensaje de si ese jugador pertenece o no al salon de la fama 
        """
        for jugador in self.jugadores_team:
            match_nombre = re.search(nombre_jugador,jugador.nombre,re.IGNORECASE)
            if "Miembro del Salon de la Fama del Baloncesto" in jugador.logros and match_nombre:
                return print(f" \n{jugador.nombre} Pertenece al Salon de la Fama \n")
        return print(f" {jugador.nombre} No pertenece al Salon de la Fama \n")

    def calcular_mayor_cantidad_rebotes(self):
        """Esta funcion se encarga de calcular el jugador con mayor cantidad de rebotes  totales ,para poder mostrar esos resultados en consola 
        Returns:
            _type_: Retorno un mensaje en pantalla para poder mostrar los rebotes de un jugador 
        """
        rebotes_maximo = None
        jugador_maximo = None
        for jugador in self.jugadores_team:
            if rebotes_maximo == None or rebotes_maximo < jugador.estadisticas.rebotes_totales:
                rebotes_maximo = jugador.estadisticas.rebotes_totales
                jugador_maximo = jugador
        return print(f"El jugador con mayor cantidad de rebotes es: {jugador_maximo.nombre} con {jugador_maximo.estadisticas.rebotes_totales} Pts.")
    
    def ordenar_listado_descendente_guarda_en_csv_json(self):
        lista_ordenada = sorted( self.jugadores_team, key = lambda jugador: jugador.estadisticas.bloqueos_totales,reverse=True)
        for  jugador_ordenado in lista_ordenada:
            print(f" {jugador_ordenado.nombre} - Bloqueos totales: {jugador_ordenado.estadisticas.bloqueos_totales}")

        try:
            with open(f"castagnola.csv", mode="w",encoding='UTF-8',newline='') as archivo_guardar:
                escribir_archivo = csv.writer(archivo_guardar)
                escribir_archivo.writerow(["Nombre","Bloqueos totales"])
                for  jugador_ordenado in lista_ordenada:
                    escribir_archivo.writerow([jugador_ordenado.nombre,jugador_ordenado.estadisticas.bloqueos_totales])
                print(f"Se creó el archivo: castagnola.csv")

            nombre_json = input('\n Ingrese el nombre del archivo json ')
            if nombre_json != "":
                with open(f"{nombre_json}.json", 'w', encoding='utf-8') as archivo_json:
                        contenido = '{'
                        for  jugador_ordenado in lista_ordenada:
                            contenido += f"{jugador_ordenado.nombre} {jugador_ordenado.estadisticas.bloqueos_totales}"
                        contenido +='}'
                        json.dump(contenido, archivo_json, ensure_ascii=False, indent=4)
                        print(f"Se creó el archivo: castagnola.json")            
            return True
        except Exception:
            print(f"Error al crear el archivos ")
            return False

    def suamr_robos_y_bloqueos_totales (self):
        lista = []
        for  jugador in self.jugadores_team:
            suma_de_totales = jugador.estadisticas.bloqueos_totales + jugador.estadisticas.robos_totales
            datos_de_sumas = f"Suma Totales: {suma_de_totales} del Jugador {jugador.nombre}"
            lista.append(datos_de_sumas)
        return lista
    
    def grabar_bb_dd(self):
        with sqlite3.connect("primer_parcial_python_1/bd_listado.db") as conexion:
            try:
                sentencia = ''' create  table personajes
                            (
                                id integer primary key autoincrement,
                                nombre_jugador text,
                                bloqueos_totales text
                            )
                        '''
                conexion.execute(sentencia)
                print("Se creo la tabla personajes")
                for jugador in self.jugadores_team:
                    suma_de_totales = jugador.estadisticas.bloqueos_totales + jugador.estadisticas.robos_totales
                    conexion.execute("insert into personajes(nombre_jugador,bloqueos_totales) values (?,?)", (jugador.nombre,suma_de_totales))
                conexion.commit()
                print("Se creo jugador")                       
            except sqlite3.OperationalError:
                print("No se creo el jugador") 
    
    def grabar_listado_posiciones_bb_dd(self):
        with sqlite3.connect("primer_parcial_python_1/bd_listado_posiciones.db") as conexion:
            try:
                
                sentencia = ''' create  table posiciones
                            (
                                id integer primary key autoincrement,
                                posicion text
                            )
                        '''
                conexion.execute(sentencia)
                print("Se creo la tabla posiciones")
                posicion_actual = []
                for jugador in self.jugadores_team:
                    if not jugador.posicion in posicion_actual:
                        print(posicion_actual)
                        conexion.execute("insert into posiciones(posicion) values (?)", (jugador.posicion,))
                    posicion_actual.append(jugador.posicion)
                conexion.commit()
                print("Se creo las posiciones")   
                
            except sqlite3.OperationalError:
                print("No se creo las posiciones")

    def porcentaje_robos_y_bloqueos_totales (self):
        acum_suma_de_totales = 0
        for  jugador in self.jugadores_team:
            suma_de_totales = jugador.estadisticas.bloqueos_totales + jugador.estadisticas.robos_totales
            acum_suma_de_totales +=  suma_de_totales
        return acum_suma_de_totales
    
    def calcular_porcentaje(self,total_acumulado):
        lista = []
        for  jugador in self.jugadores_team:
            suma_de_totales = jugador.estadisticas.bloqueos_totales + jugador.estadisticas.robos_totales
            porcentaje = (suma_de_totales*100)/total_acumulado
            porcentaje = round(porcentaje, 2)
            datos_de_porcentajes = f"{porcentaje} % del Jugador {jugador.nombre}"
            lista.append(datos_de_porcentajes)
        return lista

def quick_sort(lista:list[int]):
    if len(lista) < 2:
        return lista
    else:
        lista_copia = lista.copy()
        pivot = lista_copia.pop()
        mas_grandes = []
        mas_chicos = []
        for numero in lista_copia:
            if numero > pivot :
                mas_grandes.append(numero)
            elif numero <= pivot:
                mas_chicos.append(numero)
        return  quick_sort(mas_chicos) + [pivot] + quick_sort(mas_grandes)

def imprimir_lista (lista):
    for dato in lista:
        print (dato)

def imprimir_cant_elegida_de_datos(lista,cant_a_mostrar):
    for dato in lista[:cant_a_mostrar]:
        print (dato)

def ordenar_lista (listado):
    lista_copia = listado.copy()
    numero_aux = None
    for indice_1 in range(len(lista_copia) - 1):
        for indice_2 in range(indice_1 +1 ,len(lista_copia)):
            if lista_copia [indice_1] > lista_copia[indice_2]: 
                numero_aux = lista_copia[indice_2]
                lista_copia[indice_2] = lista_copia[indice_1]
                lista_copia[indice_1] = numero_aux
    return lista_copia

menu =\
"""
        ** Menu de opciones **

1- Mostrar la lista de todos los jugadores del Dream Team
2- Mostrar estadísticas de jugador a elegir
3- Mostrar Estadísticas de jugador a elegir y guardarlas en archivo CSV
4- Mostrar Logros de jugador a elegir 
5- Promedio de Puntos del Dream Team 
6- Mostrar si el jugador elegido pertenece al Salon de la Fama
7- Mostrar el Jugador con mayor Rebotes totales
8- Ordenar y mostrar listado de Bloqueos totales ordenados de manera Descendentes y guardar en CSV y en JSON
9- Ordena los datos por el jugador que sumando los robos totales más los bloqueos totales
10- Grabar listado de posiciones de los jugadores 
11- Salir


""" 
menu2 =\
""" 
A - Ordenar los jugadores por el valor sumado
B - Listar todos los jugadores ordenados y mostrar el porcentaje de este valor sumado
C - Mostrar cantidad de jugadres que el usuario desee 
"""
def imprimir_dato(dato: str):
    print(dato)

def validar_indice(indice:str):     
    """
    validar que el el indice es un indice valida con regex  con un patron
    retornando el indice valida 
    """ 
    if re.match(r'^(1[0-2]|[1-9])$', indice):
        return int(indice)
    
def menu_opciones()->str:
    """esta funcion imprime el menu de opciones y usa la funcion de validar si ess un entero 
    y poder hacer uso de esa varible retornandola si es true
    de caso contrario se retorna ubn mensaje aclarando el error 
    """
    imprimir_dato(menu)
    opcion_elegida = input("Elegir una opcion: ")
    if validar_indice(opcion_elegida):
        return int(opcion_elegida)
    else:
        return print("Indique un valor correcto del 1-8")

#MENU
if __name__ == "__main__":
    equipo = Equipo("primer_parcial_python_1/dream_team.json")
    while True:
        opcion = menu_opciones()
        match(opcion):
            case 1:
                equipo.obtener_nombre_y_dato()
            case 2:
                equipo.obtener_nombre_y_dato()
                indice = equipo.obtener_indice_jugador()
                equipo.estadisticas_jugadores(indice)
            case 3:
                equipo.obtener_nombre_y_dato()
                indice = equipo.obtener_indice_jugador()
                equipo.guardar_estadisticas_archivo_csv(indice)
            case 4:
                equipo.obtener_nombre_y_dato()
                nombre_a_buscar = input("Ingrese el nombre del Jugador a Buscar: ")
                equipo.buscar_jugador_nombre(nombre_a_buscar)
            case 5:
                equipo.calcular_promedio_puntos_por_partido()
                lista_desordenada = equipo.jugadores_x_nombre()
                lista_ordenada = quick_sort(lista_desordenada)
                imprimir_lista(lista_ordenada)
            case 6:
                nombre_a_buscar = input("Ingrese el nombre del Jugador que pertenece a Salon de la Fama: ")
                equipo.buscar_jugador_en_salon_fama(nombre_a_buscar)
            case 7:
                equipo.calcular_mayor_cantidad_rebotes()
            case 8:
                equipo.ordenar_listado_descendente_guarda_en_csv_json()
                equipo.grabar_bb_dd()
            case 9:
                print(menu2)
                opcion_submenu = input("Elegir una opcion: ").upper()
                match(opcion_submenu):
                    case 'A':
                        lista_datos = equipo.suamr_robos_y_bloqueos_totales()
                        lista_ordenada = ordenar_lista(lista_datos)
                        imprimir_lista(lista_ordenada)
                    case 'B':
                        acum = equipo.porcentaje_robos_y_bloqueos_totales()
                        listado_porcentajes = equipo.calcular_porcentaje(acum)
                        result = quick_sort(listado_porcentajes)
                        imprimir_lista(result)
                    case 'C':
                        lista_datos = equipo.suamr_robos_y_bloqueos_totales()
                        lista_ordenada = ordenar_lista(lista_datos)
                        cant_jugadores = int(input("Ingrese la cantidad de Jugadores a mostrar del listado: "))
                        imprimir_cant_elegida_de_datos(lista_ordenada,cant_jugadores)
            case 10:
                equipo.grabar_listado_posiciones_bb_dd()
            case 11:
                confirma=input("Confirma salida? s/n")
                if(confirma=="s"):
                    print("Salí del programa")
                    break
                confirma=input("Confirma salida? s/n")
                if(confirma=="s"):
                    print("Salí del programa")
                    break
            


