# Guiones · Modelo Base

## Episodio 01 · Tu modelo no es tu producto

**Duración:** 8:47

**ANA:** Joel, pregunta incómoda. Si te doy el mejor modelo del mundo, ¿puedo construir un producto malo?

**JOEL:** Sí. Y no es la excepción. Es la norma.

**ANA:** Véndeme eso.

**JOEL:** Piensa en la última demo de IA que viste. Alguien conecta un modelo a unos documentos, escribe una pregunta y la respuesta aparece. Todos aplauden.

**ANA:** Y tres meses después el proyecto no existe.

**JOEL:** Porque una demo demuestra que el modelo puede responder una vez. Producción exige responder diez mil veces, con datos sucios, usuarios que escriben raro y un costo que alguien tiene que pagar.

**ANA:** Entonces el modelo sí importa, pero no es lo único.

**JOEL:** El modelo es una pieza. La aplicación es el sistema. Y la mayoría de los fracasos ocurren en las otras piezas.

**ANA:** Dame el mapa.

**JOEL:** Cuatro capas. Aplicación, modelo, datos e infraestructura. La aplicación es lo que ve el usuario: la interfaz, las instrucciones, los límites.

**ANA:** La capa que todos subestiman.

**JOEL:** Siempre. Luego el modelo: el que eliges y cómo lo adaptas. Después los datos: lo que recuperas, lo que guardas, lo que usas para evaluar. Y al final la infraestructura: latencia, costo, disponibilidad.

**ANA:** ¿Y si una capa falla?

**JOEL:** El producto falla, aunque las otras tres sean perfectas. Imagina un asistente de soporte que responde bien el 92 % de las veces. Suena increíble.

**ANA:** Suena a que el 8 % te va a costar caro.

**JOEL:** Exacto. Si ese 8 % inventa una política de reembolso, no tienes un problema de modelo. Tienes un problema legal.

**ANA:** ¿Y cómo se arregla?

**JOEL:** No se arregla pidiéndole al modelo que «no alucine». Se arregla recuperando la política real desde una fuente verificable, limitando lo que puede responder y midiendo cuántas veces falla antes de publicar.

**ANA:** O sea, con sistema.

**JOEL:** Con sistema. Y para que no suene abstracto, ponle números. Una tienda en línea recibe diez mil conversaciones al mes. El asistente responde bien el 92 %.

**ANA:** Ochocientas conversaciones mal.

**JOEL:** Ochocientas. De esas, tal vez cincuenta terminan en un reclamo. Y diez en una devolución que la empresa no debía aceptar.

**ANA:** ¿Y el modelo es el culpable?

**JOEL:** El modelo hizo lo que le pediste: completar texto plausible. El sistema no le dio la política real, no verificó la respuesta y no midió el fallo. Ahí está el problema.

**ANA:** ¿Cuánto cuesta eso?

**JOEL:** Depende del negocio, pero piénsalo al revés. ¿Cuánto cuesta escribir cincuenta casos de prueba y una política clara? Mucho menos que cincuenta reclamos.

**ANA:** Y sin embargo, nadie lo hace.

**JOEL:** Porque medir no se ve en la demo. Y lo que no se ve, no se presupuesta.

**ANA:** Entonces el modelo base es como un practicante muy leído.

**JOEL:** Me gusta la analogía. Leyó casi todo internet, sabe escribir, traduce, resume. Pero acaba de llegar a tu empresa. No conoce tus precios, tus clientes ni tus procesos.

**ANA:** Y si le preguntas algo de la empresa, va a contestar con seguridad.

**JOEL:** Eso es lo peligroso. No dice «no sé». Completa. Y lo hace muy bien.

**ANA:** Por eso hay que darle contexto.

**JOEL:** Contexto, fuentes y límites. Y aquí hay una idea que conviene desarmar: el modelo base no sabe nada de tu empresa.


**ANA:** ¿Nada?

**JOEL:** Nada. No conoce tus precios, tus clientes ni tus políticas. Sabe predecir texto. Ese es su superpoder y también su límite.

**ANA:** ¿Y de dónde sale esa capacidad?

**JOEL:** De la autosupervisión. El texto ya trae la señal: el modelo aprende a predecir el siguiente token sin que nadie etiquete cada ejemplo. Con suficientes datos y cómputo, ese objetivo simple produce representaciones útiles para muchas tareas.

**ANA:** Suena a magia barata.

**JOEL:** Suena simple, y lo es. Pero simple no significa fácil. Entrenar eso cuesta millones. Usarlo cuesta mucho menos.

**ANA:** Ahí está el negocio.

**JOEL:** Ahí está el cambio. Antes, cada tarea necesitaba su propio modelo y sus propios datos etiquetados. Clasificar correos, resumir, traducir: todo dependía de marcar ejemplos a mano. Ese cuello de botella frenaba el crecimiento.

**ANA:** Y ahora un solo modelo sirve para muchas tareas.

**JOEL:** Sirve de punto de partida. No es una aplicación terminada. Se adapta con prompts, con recuperación, con ajuste fino o con una mezcla.

**ANA:** ¿Cuál elijo?

**JOEL:** Depende. Si el problema es de conocimiento, recupera. Si es de formato o conducta, ajusta. Si es de instrucciones, escribe mejor. Y si no sabes cuál es, empieza por evaluar.

**ANA:** Siempre volvemos a evaluar.

**JOEL:** Porque sin evaluación estás adivinando. Y adivinar con presupuesto ajeno es caro.

**ANA:** Dame el error típico.

**JOEL:** Empezar por «vamos a usar GPT». Es la frase que mata más proyectos de IA en México y en cualquier lado.

**ANA:** ¿Por qué?

**JOEL:** Porque la decisión ya está tomada antes de definir el problema. Y cuando el problema aparece, el equipo defiende la herramienta en lugar de resolverlo.

**ANA:** ¿Cómo se empieza bien?

**JOEL:** Con una pregunta aburrida: ¿qué decisión o tarea quieres mejorar, y cómo sabrás que mejoró? Si no puedes responder eso, no tienes un caso de uso. Tienes una demo esperando presupuesto.

**ANA:** Y si sí puedo responderlo.

**JOEL:** Entonces elige el modelo más pequeño que pase tu evaluación. No el más grande del leaderboard.

**ANA:** Eso suena a ahorrar.

**JOEL:** Suena a ingeniería. El trabajo no es entrenar desde cero. Es elegir, adaptar, evaluar e integrar. El valor se movió del entrenamiento al sistema.

**ANA:** Repite eso, que quiero guardarlo.

**JOEL:** El valor se movió del entrenamiento al sistema.

**ANA:** Me gusta. Pero tengo una objeción. Si el sistema es lo que importa, ¿para qué seguir hablando de modelos?

**JOEL:** Porque el sistema se construye alrededor de sus límites. Si no entiendes cómo funciona el modelo, no puedes diseñar los límites.

**ANA:** Bien. Entonces el siguiente episodio es sobre cómo funciona.

**JOEL:** Sí. Y empieza con algo que casi nadie mira: los tokens.

**ANA:** Suena técnico.

**JOEL:** Suena a dinero. Cada token que entra y sale se paga.

**ANA:** Con eso me quedo. Para cerrar: si alguien está por lanzar un producto de IA, ¿qué hace esta semana?

**JOEL:** Escribe diez casos reales, con la respuesta que consideraría correcta. Si no puede escribir esos diez, todavía no está listo para lanzar.

**ANA:** Diez casos. Nada más.

**JOEL:** Diez casos valen más que cien diapositivas.

**ANA:** Modelo Base. Episodio uno. El módulo completo, con ejercicios y evaluación, está en la web del curso. Enlace en las notas.

**JOEL:** No preguntes qué modelo es más grande. Pregunta qué sistema resuelve tu problema.
