# Guiones · Modelo Base

## Episodio 03 · Aprobar no es evaluar

**Duración:** 6:42

**ANA:** Joel, entrené un clasificador con noventa y cinco por ciento de exactitud. ¿Lo lanzo?

**JOEL:** Depende de qué sea el otro cinco por ciento.

**ANA:** Es solo un cinco.

**JOEL:** Si ese cinco son fraudes que dejaste pasar, no es un cinco. Es el negocio entero.

**ANA:** Siempre empiezas igual.

**JOEL:** Porque en IA un número agregado esconde la decisión. Y la decisión es lo único que importa.

**ANA:** Vamos por partes. ¿Por qué evaluar IA es distinto a evaluar software normal?

**JOEL:** Porque en software normal un test pasa o falla. En IA, dos respuestas pueden ser correctas y una tercera puede ser mejor. No hay una sola verdad.

**ANA:** Eso complica el examen.

**JOEL:** Y complica el criterio. Si no defines qué es una buena respuesta antes de medir, vas a terminar midiendo lo que sea fácil de contar.

**ANA:** Como la exactitud.

**JOEL:** Como la exactitud. Imagina un detector de fraude. El uno por ciento de las transacciones son fraudulentas. Un modelo que dice «todo está bien» acierta el noventa y nueve por ciento.

**ANA:** Y no detecta nada.

**JOEL:** Cero fraude detectado, noventa y nueve por ciento de exactitud. El número perfecto para una diapositiva y desastroso para el negocio.

**ANA:** ¿Qué se mide entonces?

**JOEL:** Precisión y recall. Recall: de todos los fraudes reales, cuántos encontró. Precisión: de todos los que marcó como fraude, cuántos lo eran.

**ANA:** Y no puedes maximizar los dos.

**JOEL:** Hay un intercambio. Si bajas el umbral, encuentras más fraudes, pero molestas a más clientes honestos. Si lo subes, al revés. La pregunta no es cuál es mejor: es cuánto cuesta cada error.

**ANA:** Eso es una decisión de producto.

**JOEL:** Bienvenida al episodio cuatro.

**ANA:** Antes, hablemos de texto. Ahí no hay etiquetas tan claras.

**JOEL:** Ahí tienes dos familias. Evaluación exacta y evaluación semántica.

**ANA:** La exacta es comparar contra una respuesta de referencia.

**JOEL:** Sí. Sirve para formato, extracción de datos, clasificación. Pero si comparas un resumen contra una plantilla, vas a suspender respuestas correctas escritas de otra forma.

**ANA:** Y la semántica compara significado.

**JOEL:** Con embeddings, con un modelo que puntúa, o con un juez humano. Es más flexible y más fácil de engañar.

**ANA:** Ahí entra el modelo como juez.

**JOEL:** Entra. Puedes usar un modelo para evaluar a otro. Ahorra tiempo y escala. Lo que no puedes es delegarle el criterio.

**ANA:** ¿Por qué no?

**JOEL:** Porque el juez tiene sesgos. Prefiere respuestas largas, prefiere la primera opción, prefiere el estilo que se parece al suyo. Y no sabe si una afirmación es verdadera.

**ANA:** Entonces no sirve.

**JOEL:** Sirve como escala, no como criterio. Úsalo para ordenar cien respuestas, no para decidir si el producto es seguro.

**ANA:** ¿Y cómo se controla el sesgo?

**JOEL:** Comparaciones por pares en lugar de notas absolutas. Cambiar el orden de las respuestas. Tener una muestra revisada por humanos. Y medir el acuerdo entre el juez y esas personas.

**ANA:** Si el juez y los humanos no coinciden, el juez está mal.

**JOEL:** O tu definición de «bueno» está mal. Las dos cosas pasan.

**ANA:** Llegamos a los benchmarks.

**JOEL:** El leaderboard. El modelo número uno. La tentación de elegir por ranking.

**ANA:** ¿Y por qué no?

**JOEL:** Porque el benchmark mide tareas que no son tu tarea. Y porque muchos benchmarks están contaminados: sus preguntas aparecieron en el texto de entrenamiento.

**ANA:** O sea, el modelo estudió el examen.

**JOEL:** Estudió el examen. Y cuando el benchmark se satura, todos sacan noventa y algo y deja de discriminar.

**ANA:** ¿Qué hago entonces?

**JOEL:** Un conjunto propio, pequeño y oculto. Cien casos reales de tu dominio, con la respuesta que tu equipo considera correcta. Y lo usas para comparar modelos, prompts y versiones.

**ANA:** ¿Cien es suficiente?

**JOEL:** Para empezar, sí. Cien casos bien elegidos te dicen más que un leaderboard de cien mil preguntas genéricas. Después crece con los fallos que aparezcan en producción.

**ANA:** Dame el error típico.

**JOEL:** Reportar un solo número. «Precisión: 92 %». Sin desglose por tipo de caso, sin latencia, sin costo, sin los casos límite.

**ANA:** Y ese número sube en la presentación y baja en producción.

**JOEL:** Siempre. Porque producción tiene usuarios que escriben con errores, preguntan fuera de tema y intentan romper el sistema.

**ANA:** ¿Cómo se evita?

**JOEL:** Tres capas. Casos fáciles para detectar regresiones. Casos límite para ver dónde se rompe. Casos adversarios para ver si aguanta un ataque. Y una revisión humana periódica.

**ANA:** Suena a trabajo continuo.

**JOEL:** Es trabajo continuo. La evaluación no es un examen final; es un proceso.

**ANA:** Cierre. Una idea.

**JOEL:** Que un benchmark mide el examen. Tu evaluación mide el trabajo.

**ANA:** Y la frase para llevar.

**JOEL:** Si no puedes explicar qué haría un buen sistema con un caso difícil, todavía no tienes una evaluación. Tienes una corazonada con formato de tabla.

**ANA:** Módulo tres: metodología de evaluación. Enlace en las notas.

**JOEL:** Y en el próximo: por qué la calidad no es un solo número.
