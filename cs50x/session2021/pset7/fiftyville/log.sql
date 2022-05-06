-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Read the description from the table crime_scene_reports
SELECT description FROM crime_scene_reports WHERE month=7 AND day=28 AND year=2020 AND street='Chamberlin Street';

-- Theft at 10:15AM, three witnesses were present, and they gave interviews
SELECT name, transcript FROM interviews WHERE month=7 AND day=28 AND year=2020;

-- Suspect fled by car within 10 minutes, ATM on Fifer Street, earliest flight on July 29, 2020
SELECT license_plate, activity, minute FROM courthouse_security_logs WHERE month=7 AND day=28 AND year=2020 AND hour=10 AND minute >= 15 AND minute <=25;

-- Find bank accounts corresponding to a Fifer Street withdraw
SELECT account_number, amount FROM atm_transactions WHERE month=7 AND day=28 AND year=2020 AND atm_location='Fifer Street' AND transaction_type='withdraw';

-- Find all calls on that day less than 60 seconds
SELECT caller, receiver, duration FROM phone_calls WHERE month=7 AND day=28 AND year=2020 AND duration < 60;

-- Find Fiftyville airport information
SELECT id, abbreviation, full_name FROM airports WHERE city='Fiftyville';

-- 8|CSF|Fiftyville Regional Airport
SELECT id, destination_airport_id, hour, minute FROM flights WHERE origin_airport_id=8 AND month=7 AND day=29 AND year=2020;

-- There is flight 36 departing at 8:20AM to destination airport id 4
-- LHR|Heathrow Airport|London
SELECT abbreviation, full_name, city FROM airports WHERE id=4;

-- Build query to find the thief
SELECT name FROM people JOIN bank_accounts ON people.id=bank_accounts.person_id WHERE people.license_plate IN
(SELECT license_plate FROM courthouse_security_logs WHERE month=7 AND day=28 AND year=2020 AND hour=10 AND minute >= 15 AND minute <=25)
AND people.phone_number IN
(SELECT caller FROM phone_calls WHERE month=7 AND day=28 AND year=2020 AND duration < 60)
AND bank_accounts.account_number IN
(SELECT account_number FROM atm_transactions WHERE month=7 AND day=28 AND year=2020 AND atm_location='Fifer Street' AND transaction_type='withdraw')
AND people.passport_number IN
(SELECT passport_number FROM passengers WHERE flight_id=36);

-- The thief is Ernest

-- Find out Ernest's personal information
-- Ernest|(367) 555-5533|5773159633|94KL13X
SELECT name, phone_number, passport_number, license_plate FROM people WHERE name='Ernest';

-- Find out who Ernest phoned to get the identity of the accomplice
SELECT caller, receiver FROM phone_calls WHERE caller='(367) 555-5533' AND month=7 AND day=28 AND year=2020 AND duration < 60;

-- The receiver is (375) 555-8161, so find out their personal information
SELECT name FROM people WHERE phone_number='(375) 555-8161';

-- The accomplice is Berthold

