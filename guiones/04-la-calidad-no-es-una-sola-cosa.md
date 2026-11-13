# Guiones · Modelo Base

## Episodio 04 · La calidad no es una sola cosa

**Duración:** 6:31

**ANA:** Joel, dime cuál es el mejor modelo. Uno solo. El que usarías tú.

**JOEL:** El que tu producto pueda pagar, a la latencia que tu usuario tolere, con la seguridad que tu negocio exija.

**ANA:** Eso no responde la pregunta.

**JOEL:** Es la respuesta. La pregunta está mal planteada.

**ANA:** Qué cómodo.

**JOEL:** No es comodidad. Es que «mejor» sin contexto no significa nada. El modelo con mejores respuestas puede ser el peor para una tienda que necesita contestar en dos segundos.

**ANA:** Entonces la calidad es relativa.

**JOEL:** La calidad es una decisión con varias dimensiones. Y si optimizas una sola, las otras te cobran la factura.

**ANA:** Dame las dimensiones.

**JOEL:** Cuatro. Calidad de respuesta, seguridad, latencia y costo. Y las cuatro compiten.

**ANA:** Empieza por calidad, que es la obvia.

**JOEL:** La obvia y la peor definida. «Buena respuesta» puede significar correcta, completa, breve, con la fuente citada, en el tono de la marca o en el formato que espera el sistema.

**ANA:** No es lo mismo un resumen que un JSON.

**JOEL:** No es lo mismo. Por eso hay que descomponer. Si tu evaluación tiene un solo criterio, no estás midiendo calidad: estás midiendo una impresión.

**ANA:** ¿Y la seguridad?

**JOEL:** Que no filtre datos, que no acepte instrucciones escondidas, que no prometa lo que no puede cumplir. Un modelo puede ser brillante y aun así decirle a un cliente que le devolvemos el dinero.

**ANA:** Eso es un problema de negocio, no de modelo.

**JOEL:** Es un problema del sistema. Y se diseña con guardrails, con permisos y con pruebas adversarias. El modelo no es la única defensa.

**ANA:** Llegamos a latencia.

**JOEL:** La dimensión que más se ignora en las demos y la que más se nota en producción.

**ANA:** ¿Cuánto es aceptable?

**JOEL:** Depende del contexto. En una búsqueda, dos segundos se sienten lentos. En un análisis que tarda veinte, el usuario espera si ve progreso. Lo que no perdona es la inconsistencia.

**ANA:** ¿Y el promedio?

**JOEL:** El promedio miente. Lo vemos en el episodio nueve. Un sistema con promedio de un segundo y una cola de ocho segundos se siente roto.

**ANA:** Costo.

**JOEL:** Cada token se paga. Y el costo no es solo la llamada al modelo: es la infraestructura, el almacenamiento, las evaluaciones y el tiempo del equipo.

**ANA:** Y el prompt influye.

**JOEL:** Mucho. Un prompt con veinte mil tokens de contexto en cada consulta multiplica el costo y la espera. Más contexto no siempre es mejor; a veces es ruido caro.

**ANA:** ¿Cómo se decide entonces?

**JOEL:** Con una métrica que casi nadie calcula: costo total por operación. No por millón de tokens. Por respuesta útil que recibe el usuario.

**ANA:** Dame un ejemplo.

**JOEL:** Un asistente en el checkout de una tienda. El modelo grande responde mejor en las pruebas: noventa y cuatro por ciento contra noventa por ciento. Pero tarda seis segundos en lugar de dos.

**ANA:** Y la gente se va.

**JOEL:** La gente se va. Cuatro puntos de calidad no compensan cuatro segundos de espera en una decisión de compra.

**ANA:** Entonces uso el modelo pequeño.

**JOEL:** O usas los dos. Enrutar es una de las decisiones más rentables: el modelo pequeño para lo común, el grande para lo difícil.

**ANA:** Pero enrutar agrega complejidad.

**JOEL:** Agrega complejidad y la tienes que evaluar. Si el enrutador se equivoca, el usuario recibe una respuesta peor sin saber por qué.

**ANA:** Hablamos de comprar o construir.

**JOEL:** API contra modelo abierto. La API te da velocidad de salida y modelos de frontera. El modelo abierto te da control, privacidad y costo fijo, pero te obliga a operarlo.

**ANA:** ¿Qué decidiría primero?

**JOEL:** Privacidad y licencia. Si tus datos no pueden salir, la discusión termina ahí. Si la licencia no permite tu uso comercial, también.

**ANA:** Y después.

**JOEL:** Después, volumen. Con poco volumen, la API suele ganar. Con volumen alto y estable, el modelo abierto puede ser más barato, si tienes equipo para operarlo.

**ANA:** Llegamos al pipeline de evaluación.

**JOEL:** La herramienta que convierte todas estas dimensiones en decisiones. Sin pipeline, cada cambio de prompt se vuelve una discusión de opiniones.

**ANA:** ¿Qué debe tener?

**JOEL:** Tres tipos de casos: fáciles, límite y adversarios. Dos formas de evaluar: automática para escala, humana para criterio. Y una regla: ningún cambio se publica sin pasar el pipeline.

**ANA:** ¿Y si el cambio mejora la calidad pero empeora la latencia?

**JOEL:** Entonces es una decisión de producto, no una decisión técnica. Y la toma alguien que vea las dos cosas.

**ANA:** Error típico.

**JOEL:** Optimizar la calidad de respuesta mientras la experiencia se cae por latencia o por costo. Es el equivalente a mejorar el motor y olvidar las llantas.

**ANA:** Cierre.

**JOEL:** Que la calidad no es un número. Es un acuerdo sobre qué sacrificas y qué no.

**ANA:** La frase.

**JOEL:** La calidad es una decisión de producto, no una puntuación.

**ANA:** Módulo cuatro: evaluar sistemas de IA. Enlace en las notas.

**JOEL:** En el próximo: el prompt no es una frase mágica. Es una especificación incompleta.
