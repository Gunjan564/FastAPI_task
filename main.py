from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import Optional

class Product(BaseModel):
    id:int = Field(...,description="id of the Product",examples="1")
    name:str = Field(...,min_length=1,description="Product's name is compulsory to mention")
    price:float=Field(...,gt=0.0,description="Price has to be greater than zero,i.e. Product cannot be free")
    quantity:int=Field(...,ge=0, description="quantity has to be a positive integer")

class ProductUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1)
    price: Optional[float] = Field(None, gt=0.0)
    quantity: Optional[int] = Field(None, ge=0)

app = FastAPI(
    title='Product Management API',
    description = 'FastAPI application for managing products'
)

# data: list[Product] = []
data: list[Product] = [
    Product(id=1, name="Wireless Mouse", price=25.99, quantity=50),
    Product(id=2, name="Mechanical Keyboard", price=85.00, quantity=30),
    Product(id=3, name="27-inch Monitor", price=299.50, quantity=15),
    Product(id=4, name="USB-C Hub", price=45.00, quantity=100)
]

@app.get('/')
def home():
    return {'message':'Hello! welcome to our Application'}

@app.post("/products/", response_model=Product, status_code=status.HTTP_201_CREATED)
def add_product(product: Product):
    for p in data:
        if p.id == product.id:
            raise HTTPException(status_code=400, detail="Product with this ID already exists.")
    data.append(product)
    return product

@app.get("/products/", response_model=list[Product])
def view_all_products():
    return data

@app.get("/products/{product_id}", response_model=Product)
def view_product(product_id: int):
    for product in data:
        if product.id == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found.")

@app.put("/products/{product_id}", response_model=Product)
def update_product(product_id: int, product_update: ProductUpdate):
    for i, product in enumerate(data):
        if product.id == product_id:
            # Update only the fields that were provided in the request
            update_data = product_update.model_dump(exclude_unset=True)
            updated_product = product.model_copy(update=update_data)
            data[i] = updated_product
            return updated_product
    raise HTTPException(status_code=404, detail="Product not found.")

@app.delete("/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: int):
    for i, product in enumerate(data):
        if product.id == product_id:
            del data[i]
            return
    raise HTTPException(status_code=404, detail="Product not found.")