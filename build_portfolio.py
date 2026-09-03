#!/usr/bin/env python3
# -*- coding: utf-8 -*-

html = r''''''<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Carlos Expósito — Senior Full Stack Developer</title>
    <meta name="description"
        content="Portafolio profesional de Carlos Expósito, desarrollador Full Stack especializado en Java, Python, JavaScript y tecnologías cloud.">
    <meta name="author" content="Carlos Expósito">
    <meta property="og:type" content="website">
    <meta property="og:title" content="Carlos Expósito — Senior Full Stack Developer">
    <meta property="og:description"
        content="Portafolio profesional de Carlos Expósito. Java · Python · JavaScript · Cloud.">
    <meta property="og:image"
        content="https://media.licdn.com/dms/image/v2/D4D03AQF4CULpdXIraw/profile-displayphoto-shrink_800_800/B4DZcMvz2GIAAc-/0/1748265549648?e=1755129600&v=beta&t=E7mVxTP3wBL4sV6YWYQNstvw3Exn6NzCYwXgScs_Gh0">
    <link rel="icon" type="image/svg+xml"
        href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>👨‍💻</text></svg>">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link
        href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Fira+Code:wght@400;500&display=swap"
        rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <link rel="stylesheet" href="style.css">
    <script type="application/ld+json">
    {"@context":"https://schema.org","@type":"Person","name":"Carlos Expósito","jobTitle":"Senior Full Stack Developer","url":"https://frodygr.github.io/","sameAs":["https://www.linkedin.com/in/carlos-exposito-ceballo","https://github.com/FrodyGr"],"email":"carlos.cjec@gmail.com","address":{"@type":"PostalAddress","addressLocality":"Barcelona","addressCountry":"ES"}}
    </script>
</head>

<body>
    <div class="cursor-glow" id="cursorGlow"></div>

    <!-- Mobile Nav -->
    <nav class="mobile-nav">
        <a href="#" class="mobile-logo">CE</a>
        <button class="hamburger" id="hamburger" aria-label="Menú">
            <span></span><span></span><span></span>
        </button>
    </nav>
    <div class="mobile-menu" id="mobileMenu">
        <a href="#about">Sobre Mí</a>
        <a href="#experience">Experiencia</a>
        <a href="#projects">Proyectos</a>
        <a href="#contact">Contacto</a>
    </div>

    <div class="layout">
        <!-- ========== LEFT COLUMN (STICKY) ========== -->
        <header class="sidebar">
            <div class="sidebar-content">
                <div class="sidebar-top">
                    <img src="foto.jpeg" alt="Carlos Expósito" class="avatar">
                    <h1 class="name">Carlos Expósito</h1>
                    <h2 class="title">Senior Full Stack Developer</h2>
                    <p class="tagline">+8 años picando código en <span
                            class="highlight">Java</span>, <span class="highlight">Python</span> y <span
                            class="highlight">JavaScript</span>. De backend pesado a frontends que no dan vergüenza.</p>
                </div>
                <nav class="sidebar-nav" aria-label="Secciones">
                    <a href="#about" class="nav-link active" data-section="about">
                        <span class="nav-indicator"></span>
                        <span class="nav-text">Sobre Mí</span>
                    </a>
                    <a href="#experience" class="nav-link" data-section="experience">
                        <span class="nav-indicator"></span>
                        <span class="nav-text">Experiencia</span>
                    </a>
                    <a href="#projects" class="nav-link" data-section="projects">
                        <span class="nav-indicator"></span>
                        <span class="nav-text">Proyectos</span>
                    </a>

                    <a href="#contact" class="nav-link" data-section="contact">
                        <span class="nav-indicator"></span>
                        <span class="nav-text">Contacto</span>
                    </a>
                </nav>
                <div class="sidebar-social">
                    <a href="https://github.com/FrodyGr" target="_blank" rel="noopener" aria-label="GitHub"><i
                            class="fab fa-github"></i></a>
                    <a href="https://www.linkedin.com/in/carlos-exposito-ceballo" target="_blank" rel="noopener"
                        aria-label="LinkedIn"><i class="fab fa-linkedin"></i></a>
                    <a href="mailto:carlos.cjec@gmail.com" aria-label="Email"><i class="fas fa-envelope"></i></a>
                    <a href="https://frodygr.itch.io/" target="_blank" rel="noopener" aria-label="itch.io"><i
                            class="fab fa-itch-io"></i></a>
                </div>
            </div>
        </header>

        <!-- ========== RIGHT COLUMN (SCROLLABLE) ========== -->
        <main class="content" id="content">

            <!-- ABOUT -->
            <section id="about" class="section" aria-label="Sobre mí">
                <div class="section-header-mobile">
                    <h2>Sobre Mí</h2>
                </div>
                <p>Empecé a programar con 14 años haciendo webs en PHP — y desde entonces no he parado.
                    Me saqué la carrera de <strong>Ingeniería Informática</strong> en la UOC mientras trabajaba,
                    y llevo más de <strong>8 años</strong> en el mundo profesional pasando por logística,
                    ciberseguridad, energía y hasta robótica.</p>
                <p>Mi día a día gira alrededor de <strong>Java</strong> y <strong>Spring Boot</strong>, pero me
                    desenvuelvo bien en <strong>Python</strong> y <strong>JavaScript</strong>. He montado cosas con
                    <strong>AWS</strong>, <strong>GCP</strong>, <strong>Docker</strong>, <strong>Kubernetes</strong>...
                    lo típico cuando trabajas con microservicios y no quieres que todo explote en producción.</p>
                <p>Fuera del trabajo me gusta cacharrear con Unreal Engine haciendo jueguecillos, el peritaje informático forense (colegiado nº 03624), montar bots de
                    Telegram con IA, y publicar librerías open source en GitHub. Básicamente, sigo programando
                    pero cosas más divertidas.</p>

                <div class="skills-cloud">
                    <h3 class="subsection-title">Stack técnico</h3>
                    <div class="skills-grid-compact">
                        <div class="skill-group">
                            <h4><i class="fas fa-code"></i> Lenguajes</h4>
                            <div class="skill-logos">
                                <div class="skill-chip"><img
                                        src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/java/java-original.svg"
                                        alt="Java"><span>Java</span></div>
                                <div class="skill-chip"><img
                                        src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg"
                                        alt="Python"><span>Python</span></div>
                                <div class="skill-chip"><img
                                        src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg"
                                        alt="JS"><span>JavaScript</span></div>
                                <div class="skill-chip"><img
                                        src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/c/c-original.svg"
                                        alt="C"><span>C</span></div>
                                <div class="skill-chip"><img
                                        src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/php/php-original.svg"
                                        alt="PHP"><span>PHP</span></div>
                                <div class="skill-chip"><img
                                        src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/bash/bash-original.svg"
                                        alt="Bash"><span>Bash</span></div>
                            </div>
                        </div>
                        <div class="skill-group">
                            <h4><i class="fas fa-tools"></i> Frameworks</h4>
                            <div class="skill-logos">
                                <div class="skill-chip"><img
                                        src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/spring/spring-original.svg"
                                        alt="Spring"><span>Spring Boot</span></div>
                                <div class="skill-chip"><img
                                        src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/react/react-original.svg"
                                        alt="React"><span>React</span></div>
                                <div class="skill-chip"><img
                                        src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/nodejs/nodejs-original.svg"
                                        alt="Node"><span>Node.js</span></div>
                            </div>
                        </div>
                        <div class="skill-group">
                            <h4><i class="fas fa-cloud"></i> Cloud & DevOps</h4>
                            <div class="skill-logos">
                                <div class="skill-chip"><img
                                        src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/amazonwebservices/amazonwebservices-plain-wordmark.svg"
                                        alt="AWS"><span>AWS</span></div>
                                <div class="skill-chip"><img
                                        src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/googlecloud/googlecloud-original.svg"
                                        alt="GCP"><span>GCP</span></div>
                                <div class="skill-chip"><img
                                        src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg"
                                        alt="Docker"><span>Docker</span></div>
                                <div class="skill-chip"><img
                                        src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/kubernetes/kubernetes-plain.svg"
                                        alt="K8s"><span>Kubernetes</span></div>
                                <div class="skill-chip"><img
                                        src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/jenkins/jenkins-original.svg"
                                        alt="Jenkins"><span>Jenkins</span></div>
                            </div>
                        </div>
                        <div class="skill-group">
                            <h4><i class="fas fa-database"></i> Bases de Datos</h4>
                            <div class="skill-logos">
                                <div class="skill-chip"><img
                                        src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg"
                                        alt="PG"><span>PostgreSQL</span></div>
                                <div class="skill-chip"><img
                                        src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original.svg"
                                        alt="MySQL"><span>MySQL</span></div>
                                <div class="skill-chip"><img
                                        src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mongodb/mongodb-original.svg"
                                        alt="Mongo"><span>MongoDB</span></div>
                                <div class="skill-chip"><img
                                        src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/oracle/oracle-original.svg"
                                        alt="Oracle"><span>Oracle</span></div>
                                <div class="skill-chip"><img
                                        src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/elasticsearch/elasticsearch-original.svg"
                                        alt="ES"><span>Elasticsearch</span></div>
                            </div>
                        </div>
                        <div class="skill-group">
                            <h4><i class="fas fa-wrench"></i> Herramientas</h4>
                            <div class="skill-logos">
                                <div class="skill-chip"><img
                                        src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg"
                                        alt="Git"><span>Git</span></div>
                                <div class="skill-chip"><img
                                        src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/gitlab/gitlab-original.svg"
                                        alt="GitLab"><span>GitLab</span></div>
                                <div class="skill-chip"><img
                                        src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/sonarqube/sonarqube-original.svg"
                                        alt="Sonar"><span>SonarQube</span></div>
                                <div class="skill-chip"><img
                                        src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/apachekafka/apachekafka-original.svg"
                                        alt="Kafka"><span>Kafka</span></div>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="education-block">
                    <h3 class="subsection-title">Formación</h3>
                    <div class="edu-item">
                        <span class="edu-year">2019 — 2024</span>
                        <div>
                            <strong>Ingeniería Informática</strong>
                            <span class="edu-school">Universitat Oberta de Catalunya (UOC)</span>
                        </div>
                    </div>
                    <div class="edu-item">
                        <span class="edu-year">2012 — 2014</span>
                        <div>
                            <strong>CFGS Administración de Sistemas Informáticos en Red</strong>
                            <span class="edu-school">IES Albarregas</span>
                        </div>
                    </div>
                </div>
            </section>

            <!-- EXPERIENCE -->
            <section id="experience" class="section" aria-label="Experiencia profesional">
                <div class="section-header-mobile">
                    <h2>Experiencia</h2>
                </div>
                <div class="group-list">

                    <a class="exp-card" href="#" aria-label="Senior Software Developer en UST España">
                        <header class="exp-date">Abr 2025 — Presente</header>
                        <div class="exp-body">
                            <h3>Senior Software Developer · <span class="company">UST España & Latam</span></h3>
                            <p>Desarrollo backend con Java y Spring Boot en entorno AWS.
                                Microservicios, pipelines CI/CD y squads ágiles internacionales.</p>
                            <div class="tags"><span>Java</span><span>Spring
                                    Boot</span><span>Microservicios</span><span>AWS</span></div>
                        </div>
                    </a>

                    <a class="exp-card" href="#" aria-label="Tech Lead en S2 Grupo">
                        <header class="exp-date">May 2023 — Ene 2025</header>
                        <div class="exp-body">
                            <h3>Tech Lead · <span class="company">S2 Grupo</span></h3>
                            <p>Lideré un equipo de 6 personas en proyectos de ciberseguridad. Me encargaba
                                de las decisiones de arquitectura (hexagonal), ElasticSearch para búsquedas masivas,
                                y daba formación técnica a clientes y equipos L2/L3.</p>
                            <div class="tags"><span>Arquitectura Hexagonal</span><span>Elasticsearch</span><span>Spring
                                    Security</span><span>CI/CD Jenkins</span></div>
                        </div>
                    </a>

                    <a class="exp-card" href="#" aria-label="Tech Lead en Selectra">
                        <header class="exp-date">Ene 2023 — May 2023</header>
                        <div class="exp-body">
                            <h3>Tech Lead · <span class="company">Selectra</span></h3>
                            <p>Lideré el equipo técnico en el sector energético. Java, PostgreSQL, Oracle
                                y mucha coordinación con negocio para sacar features a producción.</p>
                            <div class="tags"><span>Java</span><span>Oracle
                                    Database</span><span>PostgreSQL</span><span>Git</span></div>
                        </div>
                    </a>

                    <a class="exp-card" href="#" aria-label="Analista Sénior en Dematic">
                        <header class="exp-date">Feb 2020 — Ene 2023</header>
                        <div class="exp-body">
                            <h3>Analista Sénior · <span class="company">Dematic</span></h3>
                            <p>Automatización logística para almacenes de grandes clientes farmacéuticos.
                                Mucho Spring Boot, Oracle y trabajo con equipos internacionales.</p>
                            <div class="tags"><span>Oracle Database</span><span>Spring
                                    Boot</span><span>JPA</span><span>Spring Security</span></div>
                        </div>
                    </a>

                    <a class="exp-card" href="#" aria-label="Software System Engineer en KNAPP">
                        <header class="exp-date">Sep 2017 — Feb 2020</header>
                        <div class="exp-body">
                            <h3>Software System Engineer · <span class="company">KNAPP Logistics Automation</span></h3>
                            <p>Instalación y configuración de software logístico en +30 países. Viajé bastante,
                                programaba personalizaciones en Java y formaba a los clientes finales.</p>
                            <div class="tags"><span>Oracle Database</span><span>Java</span><span>Spring
                                    Boot</span><span>Unix Server</span><span>Bash</span></div>
                        </div>
                    </a>

                    <a class="exp-card" href="#" aria-label="Programador en Prakmatic">
                        <header class="exp-date">Jul 2016 — Jul 2017</header>
                        <div class="exp-body">
                            <h3>Programador · <span class="company">Prakmatic</span></h3>
                            <p>DevOps en Telefónica. Webs con PHP, JS y MySQL. Mis primeros sprints Scrum
                                y donde pillé la base de todo.</p>
                            <div class="tags">
                                <span>HTML/CSS</span><span>PHP</span><span>JavaScript</span><span>MySQL</span><span>DevOps</span>
                            </div>
                        </div>
                    </a>

                    <a class="exp-card" href="#" aria-label="IT Technician en ANSON grupo MICROMA">
                        <header class="exp-date">Mar 2014 — Oct 2015</header>
                        <div class="exp-body">
                            <h3>IT Technician · <span class="company">ANSON grupo MICROMA</span></h3>
                            <p>Atención al público, soporte técnico, mantenimiento de software para clientes, técnico de
                                hardware y formación de usuarios en nuevos sistemas.</p>
                            <div class="tags"><span>Soporte
                                    Técnico</span><span>Hardware</span><span>Software</span><span>Formación</span></div>
                        </div>
                    </a>

                </div>
                <div class="section-cta">
                    <a href="https://www.linkedin.com/in/carlos-exposito-ceballo" target="_blank" class="inline-link">
                        Ver CV Completo <i class="fas fa-arrow-right"></i>
                    </a>
                </div>
            </section>

            <!-- PROJECTS -->
            <section id="projects" class="section" aria-label="Proyectos">
                <div class="section-header-mobile">
                    <h2>Proyectos</h2>
                </div>

                <h3 class="category-title"><i class="fas fa-star"></i> Proyectos destacados</h3>
                <div class="group-list">
                    <a class="project-card" href="https://github.com/FrodyGr/scopeflow" target="_blank">
                        <div class="project-img project-icon-bg"
                            style="--bg: linear-gradient(135deg, #0c4a6e, #0369a1)">
                            <i class="fas fa-arrows-spin fa-3x" style="color: #7dd3fc"></i>
                        </div>
                        <div class="project-body">
                            <h3>ScopeFlow <span class="featured-badge">open source</span> <i class="fas fa-arrow-up-right-from-square link-icon"></i></h3>
                            <p>Librería Java 21+ para propagación de contexto entre hilos. Resuelve el problema
                                del MDC que se pierde en virtual threads. Con Spring Boot starter, bridge a
                                OpenTelemetry y Micrometer, CI/CD y 96 tests.</p>
                            <div class="tags"><span>Java 21</span><span>Spring Boot</span><span>OpenTelemetry</span><span>Apache 2.0</span></div>
                        </div>
                    </a>
                    <a class="project-card" href="https://github.com/FrodyGr/OpenAPIGuard" target="_blank">
                        <div class="project-img project-icon-bg"
                            style="--bg: linear-gradient(135deg, #1e293b, #0f172a)">
                            <i class="fas fa-shield-halved fa-3x" style="color: #f97316"></i>
                        </div>
                        <div class="project-body">
                            <h3>OpenAPIGuard <span class="featured-badge">open source</span> <i class="fas fa-arrow-up-right-from-square link-icon"></i></h3>
                            <p>Librería de validación de seguridad para specs OpenAPI. Detecta vulnerabilidades
                                del OWASP Top 10 2023 y genera reportes SARIF para CI/CD.</p>
                            <div class="tags"><span>Java</span><span>OWASP</span><span>SARIF</span><span>Security</span></div>
                        </div>
                    </a>
                    <a class="project-card" href="https://github.com/FrodyGr/Fuse" target="_blank">
                        <div class="project-img project-icon-bg"
                            style="--bg: linear-gradient(135deg, #451a03, #b45309)">
                            <i class="fas fa-bolt-lightning fa-3x" style="color: #fbbf24"></i>
                        </div>
                        <div class="project-body">
                            <h3>Fuse <span class="featured-badge">open source</span> <i class="fas fa-arrow-up-right-from-square link-icon"></i></h3>
                            <p>Librería Java ultra ligera de Circuit Breaker para microservicios. Cero dependencias en runtime (100% JDK concurrente lock-free con CAS), JAR &lt;20 KB, soporte Maven/Gradle, filtros de excepciones y listeners de estado.</p>
                            <div class="tags"><span>Java</span><span>Circuit Breaker</span><span>Microservicios</span><span>Lock-Free</span><span>Apache 2.0</span></div>
                        </div>
                    </a>
                    <a class="project-card" href="https://github.com/FrodyGr/authforge" target="_blank">
                        <div class="project-img project-icon-bg"
                            style="--bg: linear-gradient(135deg, #1e293b, #0f172a)">
                            <i class="fas fa-lock fa-3x" style="color: #38bdf8"></i>
                        </div>
                        <div class="project-body">
                            <h3>AuthForge <i class="fas fa-arrow-up-right-from-square link-icon"></i></h3>
                            <p>Starter kit de autenticación completo que hice para no repetir el mismo
                                boilerplate en cada proyecto: login, registro, OAuth2, JWT, 2FA... todo montado.</p>
                            <div class="tags"><span>Spring Security</span><span>JWT</span><span>OAuth2</span><span>2FA</span></div>
                        </div>
                    </a>
                    <a class="project-card" href="devmetrics/index.html" target="_blank">
                        <div class="project-img project-icon-bg"
                            style="--bg: linear-gradient(135deg, #0d1117, #161b22)">
                            <i class="fas fa-chart-line fa-3x" style="color: #3fb950"></i>
                        </div>
                        <div class="project-body">
                            <h3>DevMetrics Dashboard <i class="fas fa-arrow-up-right-from-square link-icon"></i></h3>
                            <p>Quería ver mis contribuciones de GitHub de forma más visual, así que monté este
                                dashboard con mapa de calor SVG y gráficos en vivo.</p>
                            <div class="tags"><span>JavaScript</span><span>REST API</span><span>CSS Grid</span><span>Chart.js</span></div>
                        </div>
                    </a>
                    <a class="project-card" href="devassistant/index.html" target="_blank">
                        <div class="project-img project-icon-bg"
                            style="--bg: linear-gradient(135deg, #1e1b4b, #312e81)">
                            <i class="fas fa-robot fa-3x" style="color: #818cf8"></i>
                        </div>
                        <div class="project-body">
                            <h3>DevAssistant AI <i class="fas fa-arrow-up-right-from-square link-icon"></i></h3>
                            <p>Un chatbot para programadores que conecta con Groq/Llama3. Lo usé para practicar
                                streaming de respuestas y parseo de markdown en tiempo real.</p>
                            <div class="tags"><span>LLM / Groq</span><span>Markdown</span><span>Async JS</span>
                            </div>
                        </div>
                    </a>
                    <a class="project-card" href="quiz-app/index.html" target="_blank">
                        <div class="project-img project-icon-bg"
                            style="--bg: linear-gradient(135deg, #064e3b, #047857)">
                            <i class="fas fa-graduation-cap fa-3x" style="color: #4ade80"></i>
                        </div>
                        <div class="project-body">
                            <h3>Quiz de conocimientos <i
                                    class="fas fa-arrow-up-right-from-square link-icon"></i></h3>
                            <p>App de trivia con preguntas dinámicas de Open Trivia, ranking local
                                y análisis de resultados. Puro JS modular.</p>
                            <div class="tags"><span>JavaScript</span><span>Open Trivia API</span><span>LocalStorage</span></div>
                        </div>
                    </a>
                    <a class="project-card" href="microexpresiones/index.html" target="_blank">
                        <div class="project-img project-icon-bg"
                            style="--bg: linear-gradient(135deg, #134e4a, #0d9488)">
                            <i class="fas fa-face-smile fa-3x" style="color: #5eead4"></i>
                        </div>
                        <div class="project-body">
                            <h3>Microexpressions Detector <i class="fas fa-arrow-up-right-from-square link-icon"></i>
                            </h3>
                            <p>Probé TensorFlow.js para reconocimiento de microexpresiones faciales
                                directamente desde la webcam. Todo corre en el navegador, sin servidor.</p>
                            <div class="tags"><span>TensorFlow.js</span><span>ML</span><span>WebCam API</span>
                            </div>
                        </div>
                    </a>
                    <a class="project-card" href="weather-app/index.html" target="_blank">
                        <div class="project-img project-icon-bg"
                            style="--bg: linear-gradient(135deg, #1e3a8a, #1d4ed8)">
                            <i class="fas fa-cloud-sun fa-3x" style="color: #93c5fd"></i>
                        </div>
                        <div class="project-body">
                            <h3>Weather App España <i class="fas fa-arrow-up-right-from-square link-icon"></i></h3>
                            <p>Mapa del tiempo de España con Leaflet.js y OpenWeather. Búscas la ciudad y
                                te sale el clima con marcadores interactivos.</p>
                            <div class="tags"><span>Leaflet.js</span><span>OpenWeather API</span><span>CSS3</span></div>
                        </div>
                    </a>
                    <a class="project-card" href="movie-app/index.html" target="_blank">
                        <div class="project-img project-icon-bg"
                            style="--bg: linear-gradient(135deg, #7f1d1d, #b91c1c)">
                            <i class="fas fa-film fa-3x" style="color: #fca5a5"></i>
                        </div>
                        <div class="project-body">
                            <h3>Movie Discovery <i class="fas fa-arrow-up-right-from-square link-icon"></i></h3>
                            <p>Buscador de películas conectado a TMDb. Búsqueda asíncrona y
                                recomendaciones.</p>
                            <div class="tags"><span>TMDb API</span><span>Async Fetch</span><span>JavaScript</span></div>
                        </div>
                    </a>
                    <a class="project-card" href="infraviz/index.html" target="_blank">
                        <div class="project-img project-icon-bg"
                            style="--bg: linear-gradient(135deg, #FF9900, #232F3E)">
                            <i class="fas fa-project-diagram fa-3x" style="color: #f8d7a0"></i>
                        </div>
                        <div class="project-body">
                            <h3>InfraViz — Cloud Visualizer <i class="fas fa-arrow-up-right-from-square link-icon"></i>
                            </h3>
                            <p>Visualizador de arquitecturas cloud con 8 diagramas AWS,
                                grafos jerárquicos y panel de detalles. Hecho con vis.js.</p>
                            <div class="tags"><span>vis.js</span><span>AWS</span><span>Cloud
                                    Architecture</span><span>Data Visualization</span></div>
                        </div>
                    </a>
                    <a class="project-card" href="javapedia/index.html" target="_blank">
                        <div class="project-img project-icon-bg"
                            style="--bg: linear-gradient(135deg, #1a1a2e, #e76f51)">
                            <i class="fas fa-coffee fa-3x" style="color: #ffcb6b"></i>
                        </div>
                        <div class="project-body">
                            <h3>JavaPedia — Enciclopedia Java <i
                                    class="fas fa-arrow-up-right-from-square link-icon"></i></h3>
                            <p>Referencia completa de Java con 20 secciones, ejemplos de código, buscador integrado
                                y soporte bilingüe (ES/EN).</p>
                            <div class="tags"><span>Java</span><span>Prism.js</span><span>SPA</span><span>i18n</span>
                            </div>
                        </div>
                    </a>
                </div>

                <!-- ===== WEBS PROFESIONALES Y CLIENTES ===== -->
                <h3 class="category-title"><i class="fas fa-globe"></i> Webs profesionales y clientes</h3>
                <div class="group-list">
                    <a class="project-card" href="https://ceanalisisdigital.es/" target="_blank">
                        <div class="project-img">
                            <img src="assets/images/ceanalisisdigital.png" alt="CE Análisis Digital">
                        </div>
                        <div class="project-body">
                            <h3>CE Análisis Digital — Peritaje Informático <i class="fas fa-arrow-up-right-from-square link-icon"></i></h3>
                            <p>Despacho profesional y plataforma web de peritaje informático forense y evidencias digitales (Colegiado nº 03624, Barcelona). Cumplimiento de cadena de custodia bajo norma ISO 27037, análisis forense de WhatsApp, ciberdelitos, informática laboral y ratificación judicial.</p>
                            <div class="tags"><span>Peritaje Informático</span><span>Forense Digital</span><span>ISO 27037</span><span>SEO</span></div>
                        </div>
                    </a>
                    <a class="project-card" href="https://transportesexpositotoledo.com/" target="_blank">
                        <div class="project-img">
                            <img src="assets/images/transportes-exposito.jpg" alt="Transportes Expósito Toledo">
                        </div>
                        <div class="project-body">
                            <h3>Transportes Expósito Toledo <i class="fas fa-arrow-up-right-from-square link-icon"></i></h3>
                            <p>Sitio web oficial de transporte urgente de mercancías 24h directo en furgoneta sin transbordos (Toledo, con cobertura en toda España y Portugal). Diseño responsive moderno, cotización rápida y SEO local.</p>
                            <div class="tags"><span>Diseño Web</span><span>Logística</span><span>Responsive</span><span>SEO Local</span></div>
                        </div>
                    </a>
                    <a class="project-card" href="https://www.ibestan.net" target="_blank">
                        <div class="project-img">
                            <img src="assets/images/ibestan.png" alt="Ibestan">
                        </div>
                        <div class="project-body">
                            <h3>Ibestan — Web profesional <i class="fas fa-arrow-up-right-from-square link-icon"></i></h3>
                            <p>Web corporativa para Ibérica de Estanqueidad, empresa industrial B2B líder en soluciones de estanqueidad técnica. Catálogo digital, diseño responsive y SEO.</p>
                            <div class="tags"><span>Web Corporativa</span><span>B2B</span><span>Diseño</span><span>Responsive</span></div>
                        </div>
                    </a>
                </div>

                <!-- ===== OTROS PROYECTOS ===== -->
                <h3 class="category-title"><i class="fas fa-code"></i> Otros proyectos</h3>
                <div class="group-list">
                    <a class="project-card" href="https://github.com/FrodyGr/java-agents-labs" target="_blank">
                        <div class="project-img project-icon-bg" style="--bg: linear-gradient(135deg, #3b0764, #6b21a8)">
                            <i class="fas fa-brain fa-3x" style="color: #c084fc"></i>
                        </div>
                        <div class="project-body">
                            <h3>Java Agents Labs <i class="fas fa-arrow-up-right-from-square link-icon"></i></h3>
                            <p>Laboratorio experimental de agentes autónomos de IA en Java 21 utilizando el framework LangChain4j e integración con LLMs de OpenAI.</p>
                            <div class="tags"><span>Java 21</span><span>LangChain4j</span><span>AI Agents</span><span>OpenAI</span></div>
                        </div>
                    </a>
                    <a class="project-card" href="https://github.com/FrodyGr/Serverless-lambda-pizza" target="_blank">
                        <div class="project-img project-icon-bg" style="--bg: linear-gradient(135deg, #431407, #9a3412)">
                            <i class="fas fa-pizza-slice fa-3x" style="color: #fb923c"></i>
                        </div>
                        <div class="project-body">
                            <h3>Serverless AWS Pizza <i class="fas fa-arrow-up-right-from-square link-icon"></i></h3>
                            <p>Arquitectura serverless en AWS con Lambda, colas SQS y Serverless Framework en Node.js para procesamiento de pedidos asíncrono.</p>
                            <div class="tags"><span>AWS Lambda</span><span>Serverless</span><span>SQS</span><span>Node.js</span></div>
                        </div>
                    </a>
                    <a class="project-card" href="https://github.com/FrodyGr/TelegramBotAi" target="_blank">
                        <div class="project-img project-icon-bg" style="--bg: linear-gradient(135deg, #172554, #1e40af)">
                            <i class="fab fa-telegram fa-3x" style="color: #60a5fa"></i>
                        </div>
                        <div class="project-body">
                            <h3>TelegramBot AI <i class="fas fa-arrow-up-right-from-square link-icon"></i></h3>
                            <p>Bot de Telegram con IA que monté desde cero. Conecta con APIs de lenguaje natural.</p>
                            <div class="tags"><span>Python</span><span>AI</span><span>Telegram</span></div>
                        </div>
                    </a>
                    <a class="project-card" href="https://github.com/FrodyGr/ELK_Example" target="_blank">
                        <div class="project-img project-icon-bg" style="--bg: linear-gradient(135deg, #1a2e05, #365314)">
                            <i class="fas fa-magnifying-glass-chart fa-3x" style="color: #84cc16"></i>
                        </div>
                        <div class="project-body">
                            <h3>ELK Stack <i class="fas fa-arrow-up-right-from-square link-icon"></i></h3>
                            <p>Setup completo de Elasticsearch + Logstash + Kibana. Docker compose incluido.</p>
                            <div class="tags"><span>Elasticsearch</span><span>Logstash</span><span>Kibana</span></div>
                        </div>
                    </a>
                    <a class="project-card" href="https://github.com/FrodyGr/loom-processing" target="_blank">
                        <div class="project-img project-icon-bg" style="--bg: linear-gradient(135deg, #422006, #92400e)">
                            <i class="fas fa-microchip fa-3x" style="color: #fbbf24"></i>
                        </div>
                        <div class="project-body">
                            <h3>Loom Virtual Threads <i class="fas fa-arrow-up-right-from-square link-icon"></i></h3>
                            <p>Benchmark threads tradicionales vs virtual threads de Java 21. Spoiler: Loom gana por goleada.</p>
                            <div class="tags"><span>Java 21</span><span>Loom</span><span>Virtual Threads</span></div>
                        </div>
                    </a>
                    <a class="project-card" href="https://github.com/FrodyGr/Websocket-Example" target="_blank">
                        <div class="project-img project-icon-bg" style="--bg: linear-gradient(135deg, #164e63, #0891b2)">
                            <i class="fas fa-comments fa-3x" style="color: #67e8f9"></i>
                        </div>
                        <div class="project-body">
                            <h3>Chat en Tiempo Real <i class="fas fa-arrow-up-right-from-square link-icon"></i></h3>
                            <p>Chat con WebSockets y Spring Boot. Nada de polling.</p>
                            <div class="tags"><span>WebSocket</span><span>Spring Boot</span><span>JavaScript</span></div>
                        </div>
                    </a>
                    <a class="project-card" href="https://github.com/FrodyGr/webrtc-videollamada" target="_blank">
                        <div class="project-img project-icon-bg" style="--bg: linear-gradient(135deg, #701a75, #a21caf)">
                            <i class="fas fa-video fa-3x" style="color: #f0abfc"></i>
                        </div>
                        <div class="project-body">
                            <h3>Videollamadas WebRTC <i class="fas fa-arrow-up-right-from-square link-icon"></i></h3>
                            <p>Videollamadas P2P con WebRTC. Sin intermediarios, conexión directa.</p>
                            <div class="tags"><span>WebRTC</span><span>Spring Boot</span><span>JavaScript</span></div>
                        </div>
                    </a>
                    <a class="project-card" href="https://github.com/FrodyGr/OrderNotification" target="_blank">
                        <div class="project-img project-icon-bg" style="--bg: linear-gradient(135deg, #1c1917, #292524)">
                            <i class="fas fa-bell fa-3x" style="color: #fb923c"></i>
                        </div>
                        <div class="project-body">
                            <h3>Kafka Order Notifications <i class="fas fa-arrow-up-right-from-square link-icon"></i></h3>
                            <p>Mini sistema de pedidos con Kafka. Productor, consumidor y notificaciones en tiempo real.</p>
                            <div class="tags"><span>Kafka</span><span>Microservicios</span><span>Java</span></div>
                        </div>
                    </a>
                    <a class="project-card" href="https://github.com/FrodyGr/BlockchainTransaction" target="_blank">
                        <div class="project-img project-icon-bg" style="--bg: linear-gradient(135deg, #312e81, #4338ca)">
                            <i class="fas fa-link fa-3x" style="color: #a78bfa"></i>
                        </div>
                        <div class="project-body">
                            <h3>Blockchain Transactions <i class="fas fa-arrow-up-right-from-square link-icon"></i></h3>
                            <p>Transacciones blockchain con criptografía en Java. Para entender cómo funciona por debajo.</p>
                            <div class="tags"><span>Blockchain</span><span>Java</span><span>Criptografía</span></div>
                        </div>
                    </a>
                    <a class="project-card" href="https://github.com/FrodyGr/LearnJavaWithMe" target="_blank">
                        <div class="project-img project-icon-bg" style="--bg: linear-gradient(135deg, #7c2d12, #c2410c)">
                            <i class="fab fa-java fa-3x" style="color: #fdba74"></i>
                        </div>
                        <div class="project-body">
                            <h3>Learn Java With Me <i class="fas fa-arrow-up-right-from-square link-icon"></i></h3>
                            <p>Curso de Java que preparé para mis alumnos. De lo básico a patrones de diseño. Mi repo con más estrellas.</p>
                            <div class="tags"><span>Java</span><span>Tutorial</span><span>Educación</span></div>
                        </div>
                    </a>
                    <a class="project-card" href="https://github.com/FrodyGr/AWSCDK-Course" target="_blank">
                        <div class="project-img project-icon-bg" style="--bg: linear-gradient(135deg, #1e3a5f, #f59e0b)">
                            <i class="fab fa-aws fa-3x" style="color: #fbbf24"></i>
                        </div>
                        <div class="project-body">
                            <h3>AWS CDK Course <i class="fas fa-arrow-up-right-from-square link-icon"></i></h3>
                            <p>Curso práctico de AWS CDK. Infraestructura como código con TypeScript, paso a paso.</p>
                            <div class="tags"><span>AWS</span><span>CDK</span><span>TypeScript</span></div>
                        </div>
                    </a>
                    <a class="project-card" href="start.html">
                        <div class="project-img project-icon-bg" style="--bg: linear-gradient(135deg, #1e1e2e, #313244)">
                            <i class="fas fa-key fa-3x" style="color: #94e2d5"></i>
                        </div>
                        <div class="project-body">
                            <h3>Escape Room 'Código Sombrío' <i class="fas fa-arrow-up-right-from-square link-icon"></i></h3>
                            <p>Escape room de programación que hice para mis clases. Puzzles de lógica y código.</p>
                            <div class="tags"><span>Juego</span><span>Puzzles</span><span>Interactivo</span></div>
                        </div>
                    </a>
                    <a class="project-card" href="https://frodygr.itch.io/cursed-cementery" target="_blank">
                        <div class="project-img">
                            <img src="assets/images/cursed-cementery.png" alt="Cursed Cemetery">
                        </div>
                        <div class="project-body">
                            <h3>Cursed Cemetery <i class="fas fa-arrow-up-right-from-square link-icon"></i></h3>
                            <p>Mi primer juego en Unreal Engine 5. Terror 3D publicado en itch.io.</p>
                            <div class="tags"><span>Unreal Engine 5</span><span>Blueprints</span><span>3D</span></div>
                        </div>
                    </a>
                </div>

            </section>



            <!-- CONTACT -->
            <section id="contact" class="section" aria-label="Contacto">
                <div class="section-header-mobile">
                    <h2>Contacto</h2>
                </div>
                <p>Si tienes algo entre manos y crees que puedo aportar, escríbeme sin compromiso.
                    Estoy abierto a proyectos interesantes, colaboraciones o simplemente charlar sobre tecnología.</p>
                <div class="contact-links">
                    <a href="mailto:carlos.cjec@gmail.com" class="contact-btn primary">
                        <i class="fas fa-envelope"></i> carlos.cjec@gmail.com
                    </a>
                    <a href="https://www.linkedin.com/in/carlos-exposito-ceballo" target="_blank" class="contact-btn">
                        <i class="fab fa-linkedin"></i> LinkedIn
                    </a>
                    <a href="https://github.com/FrodyGr" target="_blank" class="contact-btn">
                        <i class="fab fa-github"></i> GitHub
                    </a>
                </div>
                <p class="contact-meta"><i class="fas fa-map-marker-alt"></i> Barcelona, España · Trabajo remoto global
                    · Respuesta en &lt;24h</p>
            </section>

            <!-- FOOTER -->
            <footer class="footer">
                <p>Hecho a mano por Carlos Expósito — HTML, CSS y JavaScript sin frameworks.</p>
            </footer>
        </main>
    </div>

    <script>
        (function () {
            // Cursor glow
            const glow = document.getElementById('cursorGlow');
            if (window.innerWidth > 768) {
                document.addEventListener('mousemove', e => {
                    glow.style.background = `radial-gradient(600px at ${e.clientX}px ${e.clientY}px, rgba(125, 211, 252, 0.06), transparent 80%)`;
                });
            }

            // Scroll Spy
            const sections = document.querySelectorAll('.section');
            const navLinks = document.querySelectorAll('.nav-link');
            const observer = new IntersectionObserver(entries => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        navLinks.forEach(l => l.classList.remove('active'));
                        const id = entry.target.getAttribute('id');
                        const active = document.querySelector(`.nav-link[data-section="${id}"]`);
                        if (active) active.classList.add('active');
                    }
                });
            }, { rootMargin: '-20% 0px -60% 0px' });
            sections.forEach(s => observer.observe(s));

            // Mobile menu
            const hamburger = document.getElementById('hamburger');
            const mobileMenu = document.getElementById('mobileMenu');
            if (hamburger) {
                hamburger.addEventListener('click', () => {
                    hamburger.classList.toggle('active');
                    mobileMenu.classList.toggle('active');
                });
                mobileMenu.querySelectorAll('a').forEach(a => {
                    a.addEventListener('click', () => {
                        hamburger.classList.remove('active');
                        mobileMenu.classList.remove('active');
                    });
                });
            }

            // Smooth scroll
            document.querySelectorAll('a[href^="#"]').forEach(a => {
                a.addEventListener('click', e => {
                    e.preventDefault();
                    const t = document.querySelector(a.getAttribute('href'));
                    if (t) t.scrollIntoView({ behavior: 'smooth', block: 'start' });
                });
            });
        })();
    </script>
</body>

</html>''''''

css = r''''''/* ========== RESET & BASE ========== */
*,
*::before,
*::after {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

html {
    scroll-behavior: smooth;
    scroll-padding-top: 80px;
}

body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    background: #0b0f19;
    color: #9ca3af;
    line-height: 1.7;
    -webkit-font-smoothing: antialiased;
}

::selection {
    background: rgba(99, 179, 237, 0.18);
    color: #e2e8f0;
}

a {
    color: #e2e8f0;
    text-decoration: none;
    transition: color 0.2s;
}

a:hover {
    color: #7dd3fc;
}

strong {
    color: #e2e8f0;
    font-weight: 500;
}

img {
    max-width: 100%;
    display: block;
}

/* ========== CURSOR GLOW ========== */
.cursor-glow {
    position: fixed;
    inset: 0;
    z-index: 1;
    pointer-events: none;
    transition: background 0.35s ease;
}

/* ========== LAYOUT ========== */
.layout {
    display: flex;
    max-width: 1280px;
    margin: 0 auto;
    min-height: 100vh;
    position: relative;
    z-index: 2;
}

/* ========== SIDEBAR ========== */
.sidebar {
    width: 48%;
    max-width: 520px;
    position: sticky;
    top: 0;
    height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 100px 48px 48px;
}

.sidebar-content {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    height: 100%;
}

.avatar {
    width: 96px;
    height: 96px;
    border-radius: 50%;
    object-fit: cover;
    border: 3px solid #1e293b;
    margin-bottom: 20px;
    transition: border-color 0.3s, box-shadow 0.3s;
}

.avatar:hover {
    border-color: #7dd3fc;
    box-shadow: 0 0 20px rgba(125, 211, 252, 0.15);
}

.name {
    font-size: 2.7rem;
    font-weight: 700;
    color: #f1f5f9;
    line-height: 1.1;
    letter-spacing: -0.025em;
}

.title {
    font-size: 1.05rem;
    font-weight: 500;
    color: #7dd3fc;
    margin-top: 8px;
    font-family: 'Fira Code', 'Consolas', monospace;
}

.tagline {
    margin-top: 16px;
    font-size: 0.92rem;
    line-height: 1.65;
    max-width: 340px;
    color: #94a3b8;
}

.highlight {
    color: #7dd3fc;
}

/* ========== SIDEBAR NAV ========== */
.sidebar-nav {
    display: flex;
    flex-direction: column;
    gap: 4px;
    margin-top: 48px;
}

.nav-link {
    display: flex;
    align-items: center;
    gap: 16px;
    padding: 8px 0;
    font-size: 0.75rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: #475569;
    transition: all 0.3s;
}

.nav-link:hover,
.nav-link.active {
    color: #e2e8f0;
}

.nav-indicator {
    width: 32px;
    height: 1px;
    background: #475569;
    transition: all 0.3s;
}

.nav-link:hover .nav-indicator,
.nav-link.active .nav-indicator {
    width: 64px;
    background: #e2e8f0;
}

/* ========== SIDEBAR SOCIAL ========== */
.sidebar-social {
    display: flex;
    gap: 20px;
    margin-top: auto;
    padding-top: 32px;
}

.sidebar-social a {
    font-size: 1.25rem;
    color: #475569;
    transition: color 0.2s, transform 0.2s;
}

.sidebar-social a:hover {
    color: #7dd3fc;
    transform: translateY(-2px);
}

/* ========== MAIN CONTENT ========== */
.content {
    flex: 1;
    padding: 100px 48px 48px 48px;
}

/* ========== SECTIONS ========== */
.section {
    margin-bottom: 120px;
    scroll-margin-top: 80px;
}

.section p {
    margin-bottom: 16px;
}

.section-header-mobile {
    display: none;
}

/* ========== SUBSECTION ========== */
.subsection-title {
    font-size: 0.85rem;
    font-weight: 600;
    color: #94a3b8;
    margin: 40px 0 20px;
    text-transform: uppercase;
    letter-spacing: 0.08em;
}

/* ========== CATEGORY TITLE ========== */
.category-title {
    font-size: 0.8rem;
    font-weight: 700;
    color: #94a3b8;
    margin: 56px 0 16px;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    display: flex;
    align-items: center;
    gap: 10px;
}

.category-title::after {
    content: '';
    flex: 1;
    height: 1px;
    background: #1e293b;
}

.category-title i {
    color: #7dd3fc;
    font-size: 0.8rem;
}

/* ========== SKILLS GRID ========== */
.skills-grid-compact {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
    gap: 20px;
}

.skill-group h4 {
    font-size: 0.75rem;
    font-weight: 600;
    color: #7dd3fc;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-bottom: 10px;
    display: flex;
    align-items: center;
    gap: 8px;
}

.skill-group h4 i {
    font-size: 0.7rem;
    opacity: 0.7;
}

/* ========== TAGS ========== */
.tags {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
    margin-top: 8px;
}

.tags span {
    font-family: 'Fira Code', 'Consolas', monospace;
    font-size: 0.68rem;
    padding: 3px 10px;
    border-radius: 4px;
    background: rgba(125, 211, 252, 0.08);
    color: #7dd3fc;
    white-space: nowrap;
    border: 1px solid rgba(125, 211, 252, 0.06);
}

/* ========== SKILL CHIPS WITH LOGOS ========== */
.skill-logos {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-top: 8px;
}

.skill-chip {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 5px 12px 5px 6px;
    border-radius: 6px;
    background: rgba(125, 211, 252, 0.06);
    border: 1px solid rgba(125, 211, 252, 0.08);
    transition: all 0.2s;
}

.skill-chip:hover {
    background: rgba(125, 211, 252, 0.12);
    border-color: rgba(125, 211, 252, 0.2);
    transform: translateY(-1px);
}

.skill-chip img {
    width: 18px;
    height: 18px;
    border-radius: 2px;
}

.skill-chip span {
    font-family: 'Fira Code', 'Consolas', monospace;
    font-size: 0.65rem;
    color: #7dd3fc;
    white-space: nowrap;
}

/* ========== EDUCATION ========== */
.education-block {
    margin-top: 40px;
}

.edu-item {
    display: flex;
    gap: 20px;
    padding: 12px 0;
    align-items: baseline;
}

.edu-year {
    font-family: 'Fira Code', 'Consolas', monospace;
    font-size: 0.73rem;
    color: #475569;
    min-width: 110px;
    white-space: nowrap;
}

.edu-item strong {
    display: block;
    color: #e2e8f0;
}

.edu-school {
    display: block;
    font-size: 0.85rem;
    color: #7dd3fc;
    margin-top: 2px;
}

/* ========== GROUP LIST (DIM EFFECT) ========== */
.group-list {
    display: flex;
    flex-direction: column;
    gap: 4px;
}

.group-list:hover > * {
    opacity: 0.4;
    transition: opacity 0.3s;
}

.group-list:hover > *:hover {
    opacity: 1 !important;
}

/* ========== EXPERIENCE CARD ========== */
.exp-card {
    display: grid;
    grid-template-columns: 140px 1fr;
    gap: 16px;
    padding: 20px 24px;
    border-radius: 8px;
    border: 1px solid transparent;
    border-left: 3px solid transparent;
    transition: all 0.25s;
    text-decoration: none;
    color: inherit;
}

.exp-card:hover {
    background: rgba(125, 211, 252, 0.03);
    border-left-color: #7dd3fc;
    box-shadow: 0 2px 20px rgba(0, 0, 0, 0.12);
    color: inherit;
}

.exp-card:hover h3 {
    color: #7dd3fc;
}

.exp-date {
    font-family: 'Fira Code', 'Consolas', monospace;
    font-size: 0.72rem;
    color: #475569;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    padding-top: 6px;
    white-space: nowrap;
}

.exp-body h3 {
    font-size: 0.95rem;
    font-weight: 500;
    color: #e2e8f0;
    line-height: 1.4;
    transition: color 0.2s;
    margin-bottom: 8px;
}

.company {
    color: #7dd3fc;
}

.exp-body p {
    font-size: 0.85rem;
    margin-bottom: 12px;
    line-height: 1.6;
}

/* ========== PROJECT CARD ========== */
.project-card {
    display: grid;
    grid-template-columns: 120px 1fr;
    gap: 16px;
    padding: 20px 24px;
    border-radius: 8px;
    border: 1px solid transparent;
    border-left: 3px solid transparent;
    transition: all 0.25s;
    text-decoration: none;
    color: inherit;
    align-items: start;
}

.project-card:hover {
    background: rgba(125, 211, 252, 0.03);
    border-left-color: #7dd3fc;
    box-shadow: 0 2px 20px rgba(0, 0, 0, 0.12);
    color: inherit;
}

.project-card:hover h3 {
    color: #7dd3fc;
}

.project-card:hover .link-icon {
    transform: translate(2px, -2px);
}

.project-img {
    border-radius: 6px;
    overflow: hidden;
    border: 1px solid #1e293b;
    aspect-ratio: 16/10;
    transition: border-color 0.3s;
}

.project-card:hover .project-img {
    border-color: rgba(125, 211, 252, 0.25);
}

.project-img img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.project-icon-bg {
    background: var(--bg);
    display: flex;
    align-items: center;
    justify-content: center;
}

.project-body h3 {
    font-size: 0.95rem;
    font-weight: 500;
    color: #e2e8f0;
    transition: color 0.2s;
    margin-bottom: 8px;
    line-height: 1.4;
}

.link-icon {
    font-size: 0.7rem;
    display: inline-block;
    margin-left: 4px;
    transition: transform 0.2s;
    opacity: 0.6;
}

.project-body p {
    font-size: 0.83rem;
    margin-bottom: 12px;
    line-height: 1.6;
}

/* ========== FEATURED BADGE ========== */
.featured-badge {
    display: inline-flex;
    align-items: center;
    gap: 4px;
    font-family: 'Fira Code', 'Consolas', monospace;
    font-size: 0.6rem;
    color: #c084fc;
    background: rgba(192, 132, 252, 0.1);
    border: 1px solid rgba(192, 132, 252, 0.15);
    padding: 2px 8px;
    border-radius: 4px;
    margin-left: 8px;
    vertical-align: middle;
    font-weight: 500;
    letter-spacing: 0.03em;
}

/* ========== CONTACT ========== */
.contact-links {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
    margin: 24px 0;
}

.contact-btn {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 12px 24px;
    border-radius: 6px;
    border: 1px solid #1e293b;
    font-size: 0.85rem;
    font-weight: 500;
    color: #e2e8f0;
    transition: all 0.2s;
}

.contact-btn:hover {
    background: rgba(125, 211, 252, 0.05);
    border-color: #7dd3fc;
    color: #7dd3fc;
}

.contact-btn.primary {
    border-color: #7dd3fc;
    color: #7dd3fc;
}

.contact-meta {
    font-size: 0.8rem;
    color: #475569;
    margin-top: 8px;
}

.contact-meta i {
    color: #7dd3fc;
    margin-right: 4px;
}

/* ========== SECTION CTA ========== */
.section-cta {
    margin-top: 24px;
}

.inline-link {
    font-weight: 600;
    font-size: 0.9rem;
    color: #e2e8f0;
    border-bottom: 1px solid transparent;
    padding-bottom: 2px;
    transition: all 0.2s;
}

.inline-link:hover {
    color: #7dd3fc;
    border-color: #7dd3fc;
}

.inline-link i {
    transition: transform 0.2s;
    margin-left: 4px;
    font-size: 0.7rem;
}

.inline-link:hover i {
    transform: translateX(4px);
}

/* ========== FOOTER ========== */
.footer {
    padding: 60px 0 24px;
    font-size: 0.78rem;
    color: #475569;
    line-height: 1.8;
}

.footer a {
    color: #7dd3fc;
}

.footer a:hover {
    text-decoration: underline;
}

/* ========== MOBILE NAV ========== */
.mobile-nav {
    display: none;
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    padding: 16px 24px;
    background: rgba(11, 15, 25, 0.92);
    backdrop-filter: blur(12px);
    z-index: 100;
    justify-content: space-between;
    align-items: center;
}

.mobile-logo {
    font-weight: 700;
    font-size: 1.3rem;
    color: #7dd3fc;
    font-family: 'Fira Code', 'Consolas', monospace;
}

.hamburger {
    background: none;
    border: none;
    cursor: pointer;
    display: flex;
    flex-direction: column;
    gap: 5px;
    padding: 4px;
}

.hamburger span {
    width: 24px;
    height: 2px;
    background: #e2e8f0;
    transition: all 0.3s;
}

.hamburger.active span:nth-child(1) {
    transform: rotate(45deg) translate(5px, 5px);
}

.hamburger.active span:nth-child(2) {
    opacity: 0;
}

.hamburger.active span:nth-child(3) {
    transform: rotate(-45deg) translate(5px, -5px);
}

.mobile-menu {
    display: none;
    position: fixed;
    top: 0;
    right: -100%;
    width: 70%;
    max-width: 320px;
    height: 100vh;
    background: #111827;
    z-index: 99;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 32px;
    transition: right 0.4s cubic-bezier(0.77, 0, 0.175, 1);
    box-shadow: -10px 0 30px rgba(0, 0, 0, 0.4);
}

.mobile-menu.active {
    right: 0;
    display: flex;
}

.mobile-menu a {
    font-family: 'Fira Code', 'Consolas', monospace;
    font-size: 0.85rem;
    color: #e2e8f0;
    letter-spacing: 0.05em;
}

.mobile-menu a:hover {
    color: #7dd3fc;
}

/* ========== RESPONSIVE ========== */
@media (max-width: 1024px) {
    .sidebar {
        padding: 80px 32px 32px;
    }

    .content {
        padding: 80px 32px 32px;
    }

    .name {
        font-size: 2.2rem;
    }

    .exp-card,
    .project-card {
        grid-template-columns: 1fr;
    }

    .exp-date {
        padding-top: 0;
        margin-bottom: 4px;
    }
}

@media (max-width: 768px) {
    .layout {
        flex-direction: column;
    }

    .sidebar {
        position: relative;
        width: 100%;
        max-width: 100%;
        height: auto;
        padding: 100px 24px 32px;
    }

    .sidebar-nav {
        display: none;
    }

    .content {
        padding: 24px;
    }

    .mobile-nav {
        display: flex;
    }

    .mobile-menu {
        display: flex;
        right: -100%;
    }

    .section {
        margin-bottom: 60px;
    }

    .section-header-mobile {
        display: block;
        position: sticky;
        top: 0;
        z-index: 10;
        background: rgba(11, 15, 25, 0.88);
        backdrop-filter: blur(8px);
        padding: 12px 0;
        margin: -12px -24px 24px;
        padding-left: 24px;
    }

    .section-header-mobile h2 {
        font-size: 0.85rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        color: #e2e8f0;
    }

    .skills-grid-compact {
        grid-template-columns: 1fr;
    }

    .exp-card,
    .project-card {
        padding: 16px;
    }

    .project-card {
        grid-template-columns: 80px 1fr;
    }

    .edu-item {
        flex-direction: column;
        gap: 2px;
    }

    .contact-links {
        flex-direction: column;
    }

    .name {
        font-size: 2rem;
    }
}

@media (max-width: 480px) {
    .project-card {
        grid-template-columns: 1fr;
    }

    .project-img {
        max-width: 120px;
    }
}''''''

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('index.html written')

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
print('style.css written')
