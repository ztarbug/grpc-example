using System.Threading.Tasks;
using Grpc.Net.Client;
using static Grpcsample.WeatherService;
using static Grpcsample.WeatherMeasurepointRequest;
using pbc = global::Google.Protobuf.Collections;

namespace Grpcsample
{

    class Client
    {
        static async Task Main(string[] args)
        {
            
            using var channel = GrpcChannel.ForAddress("http://localhost:50051");
            var client = new WeatherServiceClient(channel);
            var req = new WeatherMeasurepointRequest();
            req.Ids.Add(1);
            req.Ids.Add(2);
            var reply = await client.GetWeatherMeasurepointAsync(req);

            Console.WriteLine("Response");
            foreach (WeatherMeasurepoint point in reply.Points) {
                Console.WriteLine(point.Id + " " + point.Name + " " + point.ObservationAirTemperature);
            }
            
        }
    }
}