use actix_web::{get, post, web, App, HttpResponse, HttpServer, Responder};
use serde::{Deserialize, Serialize};

#[derive(Deserialize, Serialize)]
struct Item {
    id: String,
    location: String,
    timestamp: u64,
    status: String,
}

#[get("/status")]
async fn status() -> impl Responder {
    HttpResponse::Ok().body("Backend is running!")
}

#[post("/item/register")]
async fn register_item(item: web::Json<Item>) -> impl Responder {
    // Here you would interact with Starknet contracts or a database
    println!("Registering item: {:?}", item);
    HttpResponse::Ok().json(item.0)
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| {
        App::new()
            .service(status)
            .service(register_item)
    })
    .bind(("127.0.0.1", 8080))?
    .run()
    .await
}
