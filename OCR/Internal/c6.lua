-- Challenge 6 - Unit Converter (temp, currency, volume)
-- Created: 24/09/2026

local function table_contains(tbl, val)
    for _, v in ipairs(tbl) do
        if v == val then return true end
    end
    return false
end

function prompt_con(ut)
    local ol, ne
    while true do
        io.write("Enter the unit your current value is in: ")
        io.flush()
        local input = io.read()
        ol = input and input:gsub("%s+", ""):lower() or ""
        if not table_contains(ut, ol) then
            print("Invalid unit! You must enter one of the following: " .. table.concat(ut, ", ") .. ".")
        else
            break
        end
    end

    while true do
        io.write("Enter the unit you want the value to be converted to: ")
        io.flush()
        local input = io.read()
        ne = input and input:gsub("%s+", ""):lower() or ""
        if not table_contains(ut, ne) then
            print("Invalid unit! You must enter one of the following: " .. table.concat(ut, ", ") .. ".")
        elseif ne == ol then
            print("Invalid input! You must enter a different unit to the one your value is already in.")
        else
            break
        end
    end

    return ol, ne
end

function prompt_val()
    while true do
        io.write("Enter the value: ")
        io.flush()
        local input = io.read()
        local num = tonumber(input)
        if num then
            return num
        else
            print("Invalid input. You must enter a number.")
        end
    end
end

function convert(mode)
    local u_type
    if mode == "temperature" then
        u_type = {"fahrenheit", "celsius", "kelvin"}
    elseif mode == "currency" then
        u_type = {"gbp", "usd", "eur"}
    elseif mode == "volume" then
        u_type = {"litres", "gallons", "cups"}
    end

    local old, new = prompt_con(u_type)
    local rvalo = prompt_val()
    local rvaln = 0.0

    if mode == "temperature" then
        if old == "fahrenheit" and new == "kelvin" then rvaln = (rvalo - 32) * 5/9 + 273.15
        elseif old == "fahrenheit" and new == "celsius" then rvaln = (rvalo - 32) * 5/9
        elseif old == "celsius" and new == "kelvin" then rvaln = rvalo + 273.15
        elseif old == "celsius" and new == "fahrenheit" then rvaln = (rvalo * 9/5) + 32
        elseif old == "kelvin" and new == "fahrenheit" then rvaln = (rvalo - 273.15) * 9/5 + 32
        elseif old == "kelvin" and new == "celsius" then rvaln = rvalo - 273.15
        end
        
        local display_old = old:sub(1,1):upper() .. old:sub(2)
        local display_new = new:sub(1,1):upper() .. new:sub(2)
        local symbol_old = (old == "kelvin") and "" or "°"
        local symbol_new = (new == "kelvin") and "" or "°"

        print(string.format("Converting %.2f%s %s to %s, you get ~%.2f%s.\n", rvalo, symbol_old, display_old, display_new, rvaln, symbol_new))
        return
    
    elseif mode == "currency" then
        if old == "gbp" and new == "usd" then rvaln = rvalo * 1.3276
        elseif old == "gbp" and new == "eur" then rvaln = rvalo * 1.1635
        elseif old == "usd" and new == "gbp" then rvaln = rvalo * 0.7532
        elseif old == "usd" and new == "eur" then rvaln = rvalo * 0.8763
        elseif old == "eur" and new == "gbp" then rvaln = rvalo * 0.8595
        elseif old == "eur" and new == "usd" then rvaln = rvalo * 1.1411
        end
        
        local display_old, display_new = old:upper(), new:upper()
        print(string.format("Converting %.2f %s to %s, you get ~%.2f.\n", rvalo, display_old, display_new, rvaln))
        return

    elseif mode == "volume" then
        if old == "litres" and new == "gallons" then rvaln = rvalo / 4.546
        elseif old == "litres" and new == "cups" then rvaln = rvalo * 4.166
        elseif old == "gallons" and new == "litres" then rvaln = rvalo * 4.546
        elseif old == "gallons" and new == "cups" then rvaln = rvalo * 16
        elseif old == "cups" and new == "litres" then rvaln = rvalo / 4.166
        elseif old == "cups" and new == "gallons" then rvaln = rvalo / 16
        end
        
        print(string.format("Converting %.2f %s to %s, you get ~%.2f.\n", rvalo, old, new, rvaln))
        return
    end
end

function main()
    while true do
        print("Welcome to the Unit Converter:")
        print("1. Temperature")
        print("2. Currency")
        print("3. Volume")
        print("4. Exit")
        io.write("Please choose an option (1, 2, 3, or 4): ")
        io.flush()
        local input = io.read()
        local b = input and input:gsub("%s+", ""):lower() or ""
        
        if b == "1" or b == "temp" or b == "temperature" then
            convert("temperature")
        elseif b == "2" or b == "currency" then
            convert("currency")
        elseif b == "3" or b == "volume" then
            convert("volume")
        elseif b == "4" or b == "exit" then
            print("Goodbye!")
            break
        else
            print("This is an invalid option.\n")
        end
    end
end

main()
