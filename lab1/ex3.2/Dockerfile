# ---- Build stage (compile) ----
FROM eclipse-temurin:21-jdk AS build
WORKDIR /app
COPY Main.java .
RUN javac Main.java

# ---- Runtime stage ----
FROM eclipse-temurin:21-jre
# Προτεινόμενες ρυθμίσεις JVM σε containers
ENV JAVA_TOOL_OPTIONS="-XX:MaxRAMPercentage=75.0 -XX:+UseContainerSupport"
WORKDIR /app
# Αντιγράφουμε μόνο ό,τι χρειάζεται για runtime
COPY --from=build /app/Main.class /app/Main.class

# Τρέχουμε ως μη-προνομιούχος χρήστης
RUN useradd -m -u 10001 appuser
USER appuser

CMD ["java", "Main"]