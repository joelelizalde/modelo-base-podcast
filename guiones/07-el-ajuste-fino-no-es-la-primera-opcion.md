# Guiones · Modelo Base

## Episodio 07 · El ajuste fino no es la primera opción

**Duración:** 6:14

**ANA:** Joel, quiero que el modelo sepa todo sobre mi empresa. ¿Lo afino?

**JOEL:** Esa es la tercera opción.

**ANA:** ¿Tercera? Pensé que era la primera.

**JOEL:** Es la que suena más impresionante. Y casi nunca es la que necesitas.

**ANA:** Entonces empiezo por el prompt.

**JOEL:** Prompt, después recuperación, después ajuste fino. Y a veces no llegas al tercero.

**ANA:** ¿Por qué?

**JOEL:** Porque el ajuste fino no está hecho para meter conocimiento. Está hecho para cambiar conducta.

**ANA:** Diferencia.

**JOEL:** Conducta es formato, tono, estilo, cómo sigue una instrucción, cómo clasifica. Conocimiento es un hecho que cambia: un precio, una política, un catálogo.

**ANA:** Y el conocimiento cambia todos los días.

**JOEL:** Todos los días. Si lo metes en los pesos, cada cambio exige otro entrenamiento. Si lo recuperas, actualizas el documento y listo.

**ANA:** Entonces, ¿para qué sirve afinar?

**JOEL:** Para que el modelo haga algo consistentemente, sin repetirlo en cada prompt. Por ejemplo, devolver siempre un JSON con un formato exacto, o mantener un tono muy específico.

**ANA:** ¿Y no basta con pedírselo?

**JOEL:** A veces sí. Si un prompt con dos ejemplos lo consigue, no afines. Afinar es caro y agrega mantenimiento.

**ANA:** ¿Cuándo lo justifica?

**JOEL:** Cuando tienes muchos ejemplos de calidad, una tarea estable y una mejora medible sobre lo que ya logras con prompt y recuperación.

**ANA:** Tres condiciones.

**JOEL:** Y una cuarta: que el ahorro o la mejora compensen el costo de operar el modelo.

**ANA:** Hablemos de memoria. Entrenar todo el modelo es caro.

**JOEL:** Entrenar todos los pesos exige guardar estados, gradientes y activaciones. Es el ajuste completo. Para un modelo grande, es caro en memoria y en tiempo.

**ANA:** Y LoRA entra aquí.

**JOEL:** LoRA es una técnica de ajuste eficiente. Congelas los pesos originales y entrenas dos matrices pequeñas que ajustan la salida. Mucho menos memoria, mucho menos tiempo.

**ANA:** ¿Y funciona igual?

**JOEL:** Para muchas tareas, sí. No es magia, pero es la forma práctica de empezar.

**ANA:** ¿Qué se entrena exactamente?

**JOEL:** Depende. LoRA tiene un rango: cuánta capacidad le das al adaptador. Más rango, más parámetros y más riesgo de sobreajustar.

**ANA:** Suena a perilla.

**JOEL:** Otra perilla. Y como todas, se valida con datos, no con intuición.

**ANA:** Llegamos a los datos.

**JOEL:** La parte que decide el resultado. La diferencia entre un ajuste útil y uno que arruina el modelo casi nunca está en el optimizador. Está en los datos.

**ANA:** ¿Qué hace bueno a un dataset de ajuste?

**JOEL:** Que sea consistente, que cubra los casos reales y que el formato sea idéntico al de inferencia. Si entrenas con un formato y sirves con otro, el modelo se confunde.

**ANA:** ¿Cuántos ejemplos?

**JOEL:** Depende de la tarea. Para formato, cientos pueden bastar. Para una conducta compleja, miles. Pero cien ejemplos excelentes valen más que diez mil mediocres.

**ANA:** ¿Y si tengo diez mil y reviso cien?

**JOEL:** Entonces tienes diez mil con errores. Y el modelo los aprende.

**ANA:** Volvemos al episodio de datos.

**JOEL:** Volvemos. Aquí solo añado una regla: separa validación desde el principio. No al final, cuando ya viste los resultados.

**ANA:** Dame un ejemplo.

**JOEL:** Un equipo quiere que el asistente responda siempre en un formato de tres campos. Prueba con prompt: ochenta por ciento de cumplimiento. Prueba con prompt y ejemplos: noventa. Afina con dos mil casos: noventa y ocho.

**ANA:** Suena a victoria.

**JOEL:** Hasta que miras el costo. El adaptador mejora cuatro puntos sobre la mejor versión con prompt. ¿Merece la pena?

**ANA:** Depende.

**JOEL:** Depende de cuánto cueste cada fallo de formato y de cuánto cueste mantener el modelo ajustado. Cuatro puntos pueden valer millones o pueden no valer nada.

**ANA:** ¿Cómo se decide?

**JOEL:** Con el mismo conjunto de evaluación, el mismo prompt y la misma métrica. Si cambias algo, no puedes atribuir la mejora.

**ANA:** Y hay que evaluar más que la tarea.

**JOEL:** Tarea, formato y seguridad. Un adaptador puede mejorar el formato y empeorar el rechazo de solicitudes peligrosas.

**ANA:** Error típico.

**JOEL:** Afinar para añadir conocimiento. La empresa cambia un precio y el modelo sigue diciendo el anterior, con seguridad.

**ANA:** Y la solución es recuperar.

**JOEL:** Recuperar y citar. El conocimiento va en la fuente, no en los pesos.

**ANA:** Cierre.

**JOEL:** Que el ajuste fino es una herramienta de conducta. No es una base de datos.

**ANA:** La frase.

**JOEL:** Si necesitas conocimiento, recupera. Si necesitas conducta, ajusta.

**ANA:** Módulo siete: ajuste fino. Enlace en las notas.

**JOEL:** En el próximo: por qué un dataset enorme puede ser peor que uno pequeño.
