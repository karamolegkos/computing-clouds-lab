#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>     // sleep
#include <curl/curl.h>

typedef struct {
    char *data;
    size_t size;
} Buffer;

static size_t write_cb(void *contents, size_t size, size_t nmemb, void *userp) {
    size_t realsize = size * nmemb;
    Buffer *mem = (Buffer *)userp;

    char *ptr = realloc(mem->data, mem->size + realsize + 1);
    if (!ptr) return 0; // out of memory
    mem->data = ptr;
    memcpy(&(mem->data[mem->size]), contents, realsize);
    mem->size += realsize;
    mem->data[mem->size] = '\0';
    return realsize;
}

int fetch_weather(const char *url) {
    CURL *curl = NULL;
    CURLcode res;
    long http_code = 0;
    int ok = 1;

    Buffer buf = {0};
    buf.data = malloc(1);
    buf.size = 0;

    curl = curl_easy_init();
    if (!curl) {
        fprintf(stderr, "curl_easy_init failed\n");
        free(buf.data);
        return 0;
    }

    struct curl_slist *headers = NULL;
    headers = curl_slist_append(headers, "Content-Type: application/json");

    curl_easy_setopt(curl, CURLOPT_URL, url);
    curl_easy_setopt(curl, CURLOPT_HTTPHEADER, headers);
    curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, write_cb);
    curl_easy_setopt(curl, CURLOPT_WRITEDATA, (void *)&buf);
    curl_easy_setopt(curl, CURLOPT_USERAGENT, "weather-c-client/1.0");
    curl_easy_setopt(curl, CURLOPT_TIMEOUT, 15L);
    curl_easy_setopt(curl, CURLOPT_FOLLOWLOCATION, 1L);

    res = curl_easy_perform(curl);
    if (res != CURLE_OK) {
        fprintf(stderr, "curl perform error: %s\n", curl_easy_strerror(res));
        ok = 0;
        goto cleanup;
    }

    curl_easy_getinfo(curl, CURLINFO_RESPONSE_CODE, &http_code);
    if (http_code >= 200 && http_code < 300) {
        printf("%s\n", buf.data ? buf.data : "");
        fflush(stdout);
    } else {
        fprintf(stderr, "HTTP %ld: %s\n", http_code, buf.data ? buf.data : "");
        ok = 0;
    }

cleanup:
    curl_slist_free_all(headers);
    curl_easy_cleanup(curl);
    free(buf.data);
    return ok;
}

int main(void) {
    const char *city    = getenv("CITY")    ? getenv("CITY")    : "Athens";
    const char *state   = getenv("STATE")   ? getenv("STATE")   : "Attiki";
    const char *country = getenv("COUNTRY") ? getenv("COUNTRY") : "gr";
    const char *key     = getenv("API_KEY"); // <- να δίνεται από ENV (καλύτερη πρακτική)

    if (!key || strlen(key) == 0) {
        fprintf(stderr, "ERROR: Missing API_KEY environment variable.\n");
        return 1;
    }

    char url[1024];
    snprintf(
        url, sizeof(url),
        "https://api.openweathermap.org/data/2.5/weather?q=%s,%s,%s&appid=%s",
        city, state, country, key
    );

    printf("Weather requester (C) started ...\n");
    fflush(stdout);

    while (1) {
        fetch_weather(url);
        sleep(60);
    }
    return 0;
}