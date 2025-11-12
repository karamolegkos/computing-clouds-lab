import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.time.Duration;

public class Main {
    static String city = "Athens";
    static String state = "Attiki";
    static String country = "gr";

    // Καλύτερα από ENV var· αν λείπει, χρησιμοποιεί το default (μόνο για demo)
    static String key = System.getenv().getOrDefault("API_KEY", "dcff3a1b197264b4ba1fb5fe20a6ca4b");

    static String url = "https://api.openweathermap.org/data/2.5/weather?q="
            + city + "," + state + "," + country + "&appid=" + key;

    static HttpClient client = HttpClient.newBuilder()
            .connectTimeout(Duration.ofSeconds(10))
            .build();

    static String fetch() {
        try {
            HttpRequest req = HttpRequest.newBuilder(URI.create(url))
                    .header("Content-Type", "application/json")
                    .GET()
                    .build();
            HttpResponse<String> resp = client.send(req, HttpResponse.BodyHandlers.ofString());
            return resp.body();
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        }
    }

    public static void main(String[] args) throws InterruptedException {
        System.out.println("Weather requester (Java) started ...");
        while (true) {
            String r = fetch();
            System.out.println(r);
            Thread.sleep(60_000);
        }
    }
}