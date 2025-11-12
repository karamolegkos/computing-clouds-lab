# ---- Build stage ----
FROM alpine:3.20 AS build
RUN apk add --no-cache build-base curl-dev
WORKDIR /app
COPY main.c .
# -O2: optimization, -static optional (βαρύτερο). Θα κρατήσουμε dynamic link για μικρότερο image.
RUN cc -O2 main.c -o weather_c -lcurl

# ---- Runtime stage ----
FROM alpine:3.20
# HTTPS certs & libcurl runtime
RUN apk add --no-cache ca-certificates libcurl && update-ca-certificates
WORKDIR /app
COPY --from=build /app/weather_c /app/weather_c

# Δημιουργία non-root χρήστη
RUN adduser -D -u 10001 appuser
USER appuser

# Τρέχουμε το binary
CMD ["/app/weather_c"]