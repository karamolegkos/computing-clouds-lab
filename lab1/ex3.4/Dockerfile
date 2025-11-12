# Ελαφρύ Node runtime
FROM node:20-alpine

# Ρυθμίσεις & φάκελος εργασίας
WORKDIR /app

# Δεν έχουμε dependencies, άρα αντιγράφουμε μόνο τον κώδικα
COPY index.js /app/index.js

# Τρέχουμε ως μη-προνομιούχος χρήστης (ο built-in "node")
USER node

# Εκκίνηση εφαρμογής
CMD ["node", "/app/index.js"]