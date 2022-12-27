
use client::weather_service_client::WeatherServiceClient;
use client::WeatherMeasurepointRequest;

pub mod client {
    tonic::include_proto!("trafikverket");
}

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    println!("Calling gRPC server");

    let mut client = WeatherServiceClient::connect("http://127.0.0.1:50051").await?;

    let mut id_vector = prost::alloc::vec::Vec::new();
    id_vector.push(1);
    id_vector.push(2);

    let req = tonic::Request::new(WeatherMeasurepointRequest{ids: id_vector});

    let resp = client.get_weather_measurepoint(req).await;
    println!("{:?}", resp);

    Ok(())
}
