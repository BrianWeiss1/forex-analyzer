using HTTP
using JSON

function grabForex(apikey::String, outputsize::Int = 30)
    symbol = "EUR/USD"
    interval = "30min"

    base_url = "https://api.twelvedata.com/time_series"
    url = "$base_url?symbol=$symbol&interval=$interval&outputsize=$outputsize&apikey=$apikey"
    
    # Send an HTTP GET request to the API
    response = HTTP.get(url)
    
    if response.status == 200
        data = JSON.parse(String(response.body))
        
        if data["status"] == "ok"
            values = data["values"]
            return values
        else
            println("API request failed: ", data["status"])
        end
    else
        println("HTTP request failed with status code: ", response.status)
    end
end

# Usage example
apikey = "d6e8542914aa439e92fceaccca1c2708"

data = grabForex(apikey, 5000)

