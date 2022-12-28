extern crate base64;
extern crate image;

use std::io::Cursor;
use image::io::Reader;

use client::weather_service_client::WeatherServiceClient;
use client::{WeatherMeasurepointRequest, CameraRequest, CameraResponse};


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


    let req = tonic::Request::new(CameraRequest{id: 1});
    let resp = client.get_camera_data(req).await.unwrap();
    let cam_response:CameraResponse = resp.into_inner();

    let image_base64 = base64::decode(&cam_response.image).unwrap();

    let img = image::load_from_memory(&image_base64.to_vec()).unwrap();
    img.save("/tmp/test.png")?;

    Ok(())
}
