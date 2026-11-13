# Guiones · Modelo Base

## Episodio 09 · La latencia media miente

**Duración:** 6:04

**ANA:** Joel, mi latencia promedio es de novecientos milisegundos. ¿Está bien?

**JOEL:** Muéstrame el p99.

**ANA:** No lo tengo. Pero el promedio es bueno.

**JOEL:** El promedio es la métrica que más miente en producción.

**ANA:** Qué dramático.

**JOEL:** Piensa en una carretera. El tiempo promedio de viaje es de veinte minutos. Pero una vez al día hay un accidente y tardas dos horas. Nadie recuerda los veinte minutos. Todos recuerdan el accidente.

**ANA:** Entonces el promedio esconde la cola.

**JOEL:** La cola es la experiencia. Y la cola es la que decide si el usuario vuelve.

**ANA:** Vamos al origen. ¿Por qué tarda un modelo?

**JOEL:** Dos fases. Prefill y decodificación.

**ANA:** Prefill es leer el prompt.

**JOEL:** Sí. Procesa todos los tokens de entrada a la vez. Es intensivo en cómputo: se aprovechan bien las GPU.

**ANA:** Y la decodificación genera token por token.

**JOEL:** Uno a uno, en secuencia. Es intensivo en memoria: hay que leer los pesos y la caché en cada paso.

**ANA:** Por eso el primer token tarda y el resto va más rápido.

**JOEL:** Por eso existe TTFT: tiempo hasta el primer token. Y TPOT: tiempo por token de salida.

**ANA:** Dos métricas distintas.

**JOEL:** Y dos problemas distintos. Si el TTFT es alto, el prompt es largo o hay cola. Si el TPOT es alto, la generación es lenta o el hardware está saturado.

**ANA:** ¿Y el throughput?

**JOEL:** Cuántos tokens por segundo produce el sistema en total. No es lo mismo que la latencia de un usuario. Puedes tener mucho throughput y mala latencia si el batching es agresivo.

**ANA:** Ahí hay un intercambio.

**JOEL:** Siempre. Agrupar solicitudes mejora la utilización y el throughput, pero puede aumentar la espera individual. La decisión depende del producto.

**ANA:** Un chatbot necesita latencia. Un proceso nocturno necesita throughput.

**JOEL:** Exacto. No optimices lo mismo para los dos.

**ANA:** Volvamos al p99.

**JOEL:** El percentil 99: el tiempo que tarda el uno por ciento más lento. Si tu p99 es siete segundos, uno de cada cien usuarios espera siete segundos.

**ANA:** Con cien mil consultas al día, mil personas.

**JOEL:** Mil personas con una mala experiencia. Y probablemente son las que más lo notan: las que escriben consultas largas, las que usan el móvil, las que están en una región con más carga.

**ANA:** ¿Por qué se forma la cola?

**JOEL:** Por varias razones. Picos de tráfico, prompts largos, reintentos, una herramienta externa lenta, el recolector de basura, un despliegue. La cola casi nunca tiene una sola causa.

**ANA:** ¿Y la caché?

**JOEL:** La caché de contexto, o KV cache, guarda el estado de los tokens ya procesados. Evita recalcular el prompt en cada paso. Sin ella, la generación sería muchísimo más lenta.

**ANA:** Pero ocupa memoria.

**JOEL:** Ocupa memoria y crece con la longitud y el número de conversaciones. Ahí está el límite práctico de muchos sistemas.

**ANA:** ¿Y la cuantización?

**JOEL:** Reducir la precisión de los pesos para que ocupen menos y se muevan más rápido. Puede bajar la memoria y mejorar la latencia, a cambio de algo de calidad.

**ANA:** ¿Cuánta calidad?

**JOEL:** Depende del modelo y del método. No lo asumas: mídelo en tu conjunto de evaluación.

**ANA:** Llegamos al costo.

**JOEL:** La mayor optimización no está en la GPU. Está en no llamar al modelo.

**ANA:** ¿Cómo?

**JOEL:** Caché de respuestas para consultas repetidas. Reglas para casos simples. Recuperación antes de generar. Y enrutamiento: mandar lo fácil a un modelo pequeño.

**ANA:** Pero enrutar mal cuesta.

**JOEL:** Cuesta calidad y complejidad. Si no puedes medir el costo de un enrutamiento incorrecto, no lo hagas.

**ANA:** Dame un ejemplo de la vida real.

**JOEL:** Un asistente con promedio de novecientos milisegundos. El equipo celebra. Pero el p99 es de siete segundos y coincide con las consultas que incluyen un documento largo.

**ANA:** Los usuarios que más necesitan ayuda.

**JOEL:** Los que más esperan. La solución no fue comprar más GPU: fue limitar el tamaño del documento, dividirlo y mostrar progreso.

**ANA:** Cambiar el producto, no el hardware.

**JOEL:** Casi siempre.

**ANA:** Error típico.

**JOEL:** Optimizar el promedio. Se mejora un cinco por ciento y la cola sigue igual. El usuario no nota nada.

**ANA:** Cierre.

**JOEL:** Que optimizar inferencia no es comprar más GPU. Es entender dónde se va el tiempo y a quién le duele.

**ANA:** La frase.

**JOEL:** Optimiza la cola, no el promedio.

**ANA:** Módulo nueve: optimización de inferencia. Enlace en las notas.

**JOEL:** En el próximo, el último: cómo se junta todo en una arquitectura que se pueda observar.
