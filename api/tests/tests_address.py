from fastapi.testclient import TestClient
from main import app
import logging

client = TestClient(app)

def test_workflow():
    # 1. Create Address A (Bangalore)
    payload_a = {
        "street": "MG Road",
        "city": "Bangalore",
        "state": "Karnataka",
        "country": "India",
        "latitude": 12.9716,
        "longitude": 77.5946
    }
    response = client.post("/addresses/", json=payload_a)
    assert response.status_code == 201
    address_a = response.json()
    print("Created Address A:", address_a)

    # 2. Create Address B (Chennai) ~300km away
    payload_b = {
        "street": "Marina Beach",
        "city": "Chennai",
        "state": "Tamil Nadu",
        "country": "India",
        "latitude": 13.0827,
        "longitude": 80.2707
    }
    response = client.post("/addresses/", json=payload_b)
    assert response.status_code == 201
    address_b = response.json()
    print("Created Address B:", address_b)

    # 3. Update Address A
    updated_payload = {"street": "Brigade Road"}
    response = client.put(f"/addresses/{address_a['id']}", json=updated_payload)
    assert response.status_code == 200
    assert response.json()["street"] == "Brigade Road"
    print("Updated Address A")

    # 4. Search within 10km of Bangalore (Should find A only)
    response = client.get("/addresses/", params={"lat": 12.97, "lon": 77.59, "distance": 10})
    assert response.status_code == 200
    results = response.json()
    print("Search results (10km):", len(results))
    assert len(results) >= 1
    assert any(a["city"] == "Bangalore" for a in results)
    assert not any(a["city"] == "Chennai" for a in results)

    # 5. Search within 500km of Bangalore (Should find both)
    response = client.get("/addresses/", params={"lat": 12.97, "lon": 77.59, "distance": 500})
    assert response.status_code == 200
    results = response.json()
    print("Search results (500km):", len(results))
    assert len(results) >= 2

    # 6. Delete Address B
    response = client.delete(f"/addresses/{address_b['id']}")
    assert response.status_code == 204
    print("Deleted Address B")
    
    # Verify deletion
    response = client.get("/addresses/") # Get all
    ids = [a["id"] for a in response.json()]
    assert address_b["id"] not in ids

    print("All tests passed!")

if __name__ == "__main__":
    test_workflow()
