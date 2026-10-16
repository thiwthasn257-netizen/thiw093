CREATE TABLE IF NOT EXISTS pets (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    type VARCHAR(50) NOT NULL,
    breed VARCHAR(100),
    age INT,
    owner_name VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS rooms (
    id INT AUTO_INCREMENT PRIMARY KEY,
    room_number VARCHAR(20) NOT NULL UNIQUE,
    room_type VARCHAR(50) NOT NULL,
    daily_rate DECIMAL(10, 2) NOT NULL,
    status VARCHAR(20) NOT NULL
);

CREATE TABLE IF NOT EXISTS bookings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    pet_id INT NOT NULL,
    room_id INT NOT NULL,
    check_in DATE NOT NULL,
    check_out DATE NOT NULL,
    status VARCHAR(20) NOT NULL,
    CONSTRAINT fk_bookings_pet FOREIGN KEY (pet_id) REFERENCES pets(id),
    CONSTRAINT fk_bookings_room FOREIGN KEY (room_id) REFERENCES rooms(id)
);

INSERT INTO pets (name, type, breed, age, owner_name)
SELECT seed.name, seed.type, seed.breed, seed.age, seed.owner_name
FROM (
    SELECT 'Lucky' AS name, 'Dog' AS type, 'Golden Retriever' AS breed, 3 AS age, 'Alex' AS owner_name
    UNION ALL SELECT 'Mimi', 'Cat', 'Persian', 2, 'Alice'
    UNION ALL SELECT 'Buddy', 'Dog', 'Poodle', 4, 'Tim'
    UNION ALL SELECT 'Luna', 'Cat', 'Siamese', 1, 'Alex'
    UNION ALL SELECT 'Max', 'Dog', 'Beagle', 5, 'Alice'
) AS seed
WHERE NOT EXISTS (SELECT 1 FROM pets);

INSERT INTO rooms (room_number, room_type, daily_rate, status)
SELECT seed.room_number, seed.room_type, seed.daily_rate, seed.status
FROM (
    SELECT 'R101' AS room_number, 'Standard' AS room_type, 300.00 AS daily_rate, 'Available' AS status
    UNION ALL SELECT 'R102', 'Standard', 300.00, 'Available'
    UNION ALL SELECT 'R201', 'Deluxe', 500.00, 'Available'
    UNION ALL SELECT 'R202', 'Deluxe', 500.00, 'Available'
    UNION ALL SELECT 'R301', 'VIP', 800.00, 'Available'
) AS seed
WHERE NOT EXISTS (SELECT 1 FROM rooms);

INSERT INTO bookings (pet_id, room_id, check_in, check_out, status)
SELECT seed.pet_id, seed.room_id, seed.check_in, seed.check_out, seed.status
FROM (
    SELECT 1 AS pet_id, 1 AS room_id, '2026-10-15' AS check_in, '2026-10-17' AS check_out, 'Confirmed' AS status
    UNION ALL SELECT 2, 3, '2026-10-18', '2026-10-20', 'Confirmed'
    UNION ALL SELECT 3, 2, '2026-10-21', '2026-10-23', 'Pending'
    UNION ALL SELECT 4, 4, '2026-10-24', '2026-10-26', 'Confirmed'
    UNION ALL SELECT 5, 5, '2026-10-27', '2026-10-29', 'Pending'
) AS seed
WHERE NOT EXISTS (SELECT 1 FROM bookings);
