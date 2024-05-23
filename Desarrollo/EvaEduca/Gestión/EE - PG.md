**Plan de Gestión**
**



<a name="_gjdgxs"></a>		**Proyecto EvaEduca: Plataforma educativa con asistente virtual y autoevaluación AI** 


<a name="_h3gsjmnnllqr"></a>**Versión 1.2**



**Historial de Revisiones**

|**Fecha**|**Versión**|**Descripción**|**Autor**|
| - | - | - | - |
|4/05/2024|1\.0|Versión preliminar como una propuesta de desarrollo.|Jefe de proyecto|
|13/05/2024|1\.1|Desarrollo del documento|Jefe de proyecto|
|23/05/2024|1\.2|Modificación de contenido: Definición de nomenclatura, clasificación|Jefe de proyecto|
|||||
|||||
|||||
|||||


_

**Índice**

1. Introducción
1. Gestión de Documentos

   2.1. Definición de roles:

   2.2. Herramientas de gestión de la configuración:

   2.3. Herramienta elegida:

1. Actividades de la Gestión

   3.1. Identificación:

      3.1.1. Clasificación:

      3.1.2. Definición de nomenclatura:

      3.1.3. Diseño de repositorio:

      3.1.4. Línea base:

1. Referencias
1. Anexos


_
1. **Introducción**

IrisTech es una empresa de tecnología fundada en el año 2010, con más de una década de experiencia en el desarrollo de soluciones innovadoras para el sector educativo. Nos especializamos en proyectos que buscan mejorar la calidad y la eficiencia en la enseñanza y el aprendizaje, utilizando la tecnología como herramienta fundamental para lograrlo.

Durante nuestra trayectoria, hemos trabajado en una amplia variedad de proyectos, desde sistemas de gestión educativa hasta plataformas de aprendizaje en línea y aplicaciones móviles para la educación. Nuestro enfoque se centra en entender las necesidades específicas de nuestros clientes y diseñar soluciones a medida que se adapten a sus requerimientos y objetivos.

Sin embargo, a lo largo de nuestros proyectos, hemos enfrentado desafíos recurrentes que han afectado el éxito y la eficiencia de nuestras implementaciones. Problemas como la falta de comunicación efectiva, la gestión inadecuada de los recursos y la falta de alineación entre los equipos han sido obstáculos que hemos enfrentado en el pasado y que buscamos abordar de manera proactiva en el futuro.

Por esta razón, nos hemos propuesto implementar las mejores prácticas de Gestión de Proyectos para garantizar el éxito de nuestro próximo proyecto, EvaEduca. Nuestro objetivo es aplicar métodos y procesos estandarizados que nos permitan gestionar de manera eficiente los recursos, minimizar los riesgos y asegurar la entrega oportuna y exitosa de la plataforma educativa. Con este enfoque, esperamos superar los desafíos pasados y alcanzar nuevos niveles de excelencia en la industria de la tecnología educativa.

2. **Gestión de Documentos**
   
   2.1. **Definición de roles:**


|**Rol**|**Encargado**|**Descripción**|
| - | - | - |
|**Gestor de la configuración**|Jefe de proyecto, arquitecto de software|Responsable principal de planificar, coordinar y supervisar todas las actividades relacionadas con la gestión de la configuración de software. Se asegura de que se sigan los procesos y procedimientos establecidos.|
|**Bibliotecario de configuración**|Jefe de proyecto|<p>Define y da mantenimiento a las bibliotecas que son usadas durante </p><p>la gestión de configuración. </p><p>Es el encargado de asegurarse que los aspectos prácticos de la </p><p>gestión de configuración trabajen entre sí adecuadamente.</p>|
|**Auditor de configuración**|Jefe de proyecto, analista funcional|Realiza revisiones periódicas para garantizar que se cumplan los estándares y procedimientos de gestión de la configuración. Identifica áreas de mejora y asegura la conformidad con los requisitos.|
|**Especialista en control de cambios**|Jefe de proyecto, analista funcional, testers|Responsable de evaluar y aprobar cambios propuestos en la configuración. Evalúa el impacto de los cambios, asegura la calidad de las modificaciones y aprueba su implementación.|


   2.2. **Herramientas de gestión de la configuración:**


<table><tr><th valign="bottom"><b>Herramienta</b></th><th valign="bottom"><b>Fuente</b></th><th valign="bottom"><b>Características</b></th></tr>
<tr><td rowspan="6"><b>GitHub</b></td><td rowspan="6">[<b>https://github.com/</b>]</td><td>- Control de versiones</td></tr>
<tr><td>- Gestión de ramas y fusiones</td></tr>
<tr><td>- Seguimiento de problemas (issues)</td></tr>
<tr><td>- Integración con otros servicios (CI/CD, Notificaciones)</td></tr>
<tr><td>- Colaboración y revisión de código</td></tr>
<tr><td>- Gestión de permisos y acceso</td></tr>
<tr><td rowspan="6"><b>GitLab</b></td><td rowspan="6">[<b>https://about.gitlab.com/</b>]</td><td>- Control de versiones</td></tr>
<tr><td>- Gestión de ramas y fusiones</td></tr>
<tr><td>- Seguimiento de problemas (issues)</td></tr>
<tr><td>- Integración con otros servicios (CI/CD, Notificaciones)</td></tr>
<tr><td>- Colaboración y revisión de código</td></tr>
<tr><td>- Gestión de permisos y acceso</td></tr>
<tr><td rowspan="6"><b>Bitbucket</b></td><td rowspan="6">[<b>https://bitbucket.org/</b>]</td><td>- Control de versiones</td></tr>
<tr><td>- Gestión de ramas y fusiones</td></tr>
<tr><td>- Seguimiento de problemas (issues)</td></tr>
<tr><td>- Integración con otros servicios (CI/CD, Notificaciones)</td></tr>
<tr><td>- Colaboración y revisión de código</td></tr>
<tr><td>- Gestión de permisos y acceso</td></tr>
<tr><td rowspan="5"><b>SVN (Subversion)</b></td><td rowspan="5">[<b>https://subversion.apache.org/</b>]</td><td>- Control de versiones</td></tr>
<tr><td>- Gestión de ramas y etiquetas</td></tr>
<tr><td>- Soporte para archivos binarios y grandes repositorios</td></tr>
<tr><td>- Seguridad y autenticación</td></tr>
<tr><td>- Gestión de permisos y acceso</td></tr>
<tr><td rowspan="5"><b>Mercurial (Hg)</b></td><td rowspan="5">[<b>https://www.mercurial-scm.org/</b>]</td><td>- Control de versiones</td></tr>
<tr><td>- Gestión de ramas y etiquetas</td></tr>
<tr><td>- Soporte para distribución de repositorios</td></tr>
<tr><td>- Rendimiento y eficiencia</td></tr>
<tr><td>- Gestión de permisos y acceso</td></tr>
<tr><td rowspan="5"><b>Azure DevOps</b></td><td rowspan="5">[<b>https://azure.microsoft.com/es-es/</b>]</td><td>- Control de versiones (Repositorios Git y TFVC)</td></tr>
<tr><td>- Integración con pipelines de CI/CD</td></tr>
<tr><td>- Seguimiento de problemas (boards)</td></tr>
<tr><td>- Integración con herramientas de desarrollo (VS Code, Eclipse)</td></tr>
<tr><td>- Gestión de permisos y acceso</td></tr>
</table>


2.3. **Herramienta elegida: GitHub**

El siguiente diagrama explica de manera simplificada cómo utilizamos nuestra herramienta de control de versiones elegida para realizar operaciones con los ítems del repositorio de GitHub.

![alt text](Imágenes/Diagrama_Arquitectura.png)

3. **Actividades de la Gestión**

   3.1. **Identificación:**

   3.1.1. **Clasificación:**

Como referencia hemos tomado nuestro cronograma de proyecto elaborado (Ver anexo 1), por lo tanto clasificaremos los ítems de acuerdo a su tipo de ítem, estos tipos de ítems pueden ser:

1. **Ítems de tipo evolutivo,** tales como documentos, los que están sujetos a una o más revisiones y nuevas liberaciones durante el ciclo de vida del software. Los Items en evolución son de dos tipos: Documentos, y archivos ejecutables o de soporte.

1. **Ítems de tipo fuente,** generalmente código fuente y archivos objeto utilizados  para compilar una aplicación de software para ambiente de producción, los cuales son generalmente numerosos y cambian frecuentemente.

1. **Ítems de tipo soporte:** como sistemas operativos y software base, de los cuales el proyecto requiere ciertas versiones para su operación exitosa.

Para la clasificación de items, se tomó la siguiente regla de asignación:

- E = Ítem de tipo evolutivo
- F = Ítem de tipo fuente
- S = Ítem de tipo soporte

<table><tr><th><b>Tipo</b></th><th><b>Items</b></th><th><b>Fuente (E=Empresa, P=Proyecto, C=Cliente, V=Proveedor)</b></th><th><b>Extensión</b></th><th><b>Proyecto</b></th></tr>
<tr><td>E</td><td valign="bottom">Plan de Gestión de la Configuración de Software</td><td valign="bottom">E</td><td valign="bottom">.DOCX</td><td>-</td></tr>
<tr><td>E</td><td valign="bottom">Plan de Proyecto</td><td valign="bottom">P</td><td valign="bottom">.DOCX</td><td rowspan="16">EvaEduca</td></tr>
<tr><td>E</td><td valign="bottom">Cronograma del Proyecto</td><td valign="bottom">P</td><td valign="bottom">.XLSX</td></tr>
<tr><td>E</td><td valign="bottom">Documento de negocio</td><td valign="bottom">P</td><td valign="bottom">.DOCX</td></tr>
<tr><td>E</td><td valign="bottom">Documento de Especificación de Requisitos: Actores</td><td valign="bottom">P</td><td valign="bottom">.DOCX</td></tr>
<tr><td>E</td><td valign="bottom">Documento de Especificación de Requisitos: Casos de Uso</td><td valign="bottom">P</td><td valign="bottom">.DOCX</td></tr>
<tr><td>E</td><td valign="bottom">Documento de Especificación de UI</td><td valign="bottom">P</td><td valign="bottom">.DOCX</td></tr>
<tr><td>E</td><td valign="bottom">Documento de Guía de Estilos</td><td valign="bottom">P</td><td valign="bottom">.DOCX</td></tr>
<tr><td>E</td><td valign="bottom">Documento de Especificación de la BD</td><td valign="bottom">P</td><td valign="bottom">.DOCX</td></tr>
<tr><td>E</td><td valign="bottom">Documento de Arquitectura del Software</td><td valign="bottom">P</td><td valign="bottom">.DOCX</td></tr>
<tr><td>E</td><td valign="bottom">Reporte del Desarrollo del Software</td><td valign="bottom">P</td><td valign="bottom">.DOCX</td></tr>
<tr><td>F</td><td valign="bottom">Reporte del Primer Sprint</td><td valign="bottom">P</td><td valign="bottom">.DOCX</td></tr>
<tr><td>F</td><td valign="bottom">Reporte del Segundo Sprint</td><td valign="bottom">P</td><td valign="bottom"></td></tr>
<tr><td>E</td><td valign="bottom">Manual de usuario</td><td valign="bottom">P</td><td valign="bottom">.DOCX</td></tr>
<tr><td>E</td><td valign="bottom">Documento de Pruebas del Software</td><td valign="bottom">p</td><td valign="bottom">.DOCX</td></tr>
<tr><td>F</td><td valign="bottom">Reporte del Tercer Sprint</td><td valign="bottom">P</td><td valign="bottom">.DOCX</td></tr>
<tr><td>F</td><td valign="bottom">Acta de cierre del proyecto</td><td valign="bottom">P</td><td valign="bottom">.DOCX</td></tr>
</table>



3.1.2. **Definición de nomenclatura:**

Hemos tomado los siguientes criterios o normas para gestionar adecuadamente nuestros ítems en el repositorio de GitHub con el propósito de mejorar el tiempo de respuesta de la identificación de ítems por parte del equipo:

- **Regla N°1** = "Acronimo del proyecto" + " - " + "Acronimo de Item"

Por ejemplo, **“**EE-DN” es la forma en que la regla de asignación nos permite expresar el ítem de documento de negocio (DN) que pertenece al proyecto EvaEduca(EE).

- **Regla N°2** : Cada línea base será denominada como LB (Acrónimo de Línea Base) seguido de su número correspondiente, por ejemplo:

*LB1 = Línea Base 1*

- **Regla N°3:** Las versiones y revisiones del documento se encontrarán dentro de cada uno en una tabla que especificará qué actualizaciones se han hecho hasta la fecha. Para identificar la versión y revisión utilizaremos identificadores numéricos separados por un punto; se presentaría de la siguiente forma:

**Versión.Revisión**

El número de versión cambiará cuando se modifique la arquitectura principal del ítem o cuando el ítem es completamente reconstruido. Asimismo, el número de revisión cambiará cuando el contenido haya cambiado pero no la estructura principal o el flujo del ítem.

3.1.3. **Diseño de repositorio:**

La estructura que vamos a seguir para el diseño de repositorio será la siguiente:

- **Cliente:** Donde se encontrarán todos los ítems relacionados al cliente:
- **Desarrollo:** Donde se encontrarán todos los ítems para el desarrollo del proyecto:
  - Nombre de Proyecto
    - **Gestión:** Ítems necesarios para gestionar la organización del proyecto.
    - **Negocio:** Ítems relacionados a explicar el negocio o funcionamiento del proyecto.
    - **Análisis:** Ítems donde se analizarán los casos de uso, requisitos funcionales, no funcionales, etc.
    - **Diseño:** Ítems para evaluar el diseño de la base de datos, diseños UX/UI, entre otros relacionados.
- **Documentos**
- **Línea Base:** Donde se encontrarán todos los documentos aprobados de acuerdos  los hitos del proyecto. El número de hitos define el número de líneas base que tendrá el proyecto.
  - Nombre de proyecto
    - **Línea base 1**
    - **Línea base 2**
    - **…**
    - **Línea base n**

3.1.4. **Línea base:**

Para cada artefacto de cada hito en específico nos basamos en nuestro cronograma de proyecto (Ver anexo 1). Las líneas bases tendrán los siguientes artefactos:

|**Línea Base**|**Hito - Fecha**|**Artefactos**|
| :-: | :-: | :-: |
|LB1|1 - 10/05/2024|EE - PC, EE-CP, EE-RGH, EE-DN, EE-DERA, EE-DERCU-01, EE-DERCU-02, EE-DERCU-03, EE-DERCU-04, EE-DERCU-05, EE-DERCU-06, EE-DERCU-07, EE-DERCU-08, EE-DERCU-09, EE-DERCU-10, EE-DERCU-11, EE-DERCU-12, EE-DERCU-13, EE-DERCU-14, EE-DERCU-15, EE-DEUI, EE-DGE, EE-DEBD, EE-DAS, EE-RDS, EE-RPS.|
|LB2|2 - 20/06/2024 |Artefactos de la LB1, junto con nuevos documentos y actualización de documentos antiguos: EE-DER, EE-DEUI, EE-DEBD, EE-RDS, EE-RSS.|
|LB3|3 - 04/07/2024|Artefactos de la LB2, junto con nuevos documentos y actualización de documentos antiguos: EE-DER, EE-DEUI, EE-DEBD, EE-DAS, EE-DGE, EE-MU, EE-DPS, EE-RDS, EE-RTS, EE-ACP.|


4. **Referencias:**

GitHub. (s.f.). Recuperado de https://github.com/

GitLab. (s.f.). Recuperado de https://about.gitlab.com/

Bitbucket. (s.f.). Recuperado de https://bitbucket.org/

Apache Subversion. (s.f.). Recuperado de https://subversion.apache.org/

Mercurial. (s.f.). Recuperado de https://www.mercurial-scm.org/

Microsoft Azure. (s.f.). Recuperado de https://azure.microsoft.com/es-es/

5. **Anexos:**

-  [EE - CP - Referencia](https://docs.google.com/spreadsheets/d/1O6We5cEsoDl1SKwUSzVfVcWAyT-x4hBt2O_8ngXO9AA/edit?usp=sharing)
