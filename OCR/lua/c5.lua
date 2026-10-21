-- Challenge 5 - Fruit Machine
-- Created: 13/09/2026
-- Last Updated: 13/09/2026

math.randomseed(os.time())

function main()
    local symbols = {"Cherry", "Bell", "Lemon", "Orange", "Star", "Skull"}
    local credit = 100
    
    while true do
        print(string.format("Credit: £%.2f", credit / 100))
        io.write("Roll the fruit machine? (yes/no): ")
        io.flush()
        local roll = io.read():gsub("%s+", ""):lower()
        
        if roll == "no" or roll == "n" then
            print("Goodbye!")
            break
        elseif roll ~= "yes" and roll ~= "y" then
            print("Invalid input.\n")
            goto continue
        end

        credit = credit - 20
        print()
        
        local random_three = {}
        for i = 1, 3 do
            random_three[i] = symbols[math.random(1, #symbols)]
        end

        local r1, r2, r3 = table.unpack(random_three)

        print(string.format("Fruit Machine: %s - %s - %s", r1, r2, r3))

        if r1 == r2 and r2 == r3 then
            if r1 == "Skull" then
                credit = 0
                print("You rolled 3 Skulls - you lost all your credit!")
            elseif r1 == "Bell" then
                credit = credit + 500
                print("You rolled 3 Bells - you earned 500 credit!")
            else
                credit = credit + 100
                local plural
                if r1 == "Cherry" then
                    plural = "Cherries"
                else
                    plural = r1 .. "s" -- Fix: string concatenation uses ".."
                end
                print(string.format("You rolled 3 %s - you earned 100 credit!", plural))
            end        
        elseif r1 == r2 or r2 == r3 or r1 == r3 then
            local skull_count = 0
            for _, v in ipairs(random_three) do
                if v == "Skull" then skull_count = skull_count + 1 end
            end

            if skull_count == 2 then
                credit = math.max(0, credit - 100)
                print("You rolled 2 Skulls - you lost 100 credit!")
            else
                credit = credit + 50
                print("You rolled 2 of the same object - you earned 50 credit!")
            end
        end

        if credit < 20 then
            print()
            print(string.format("Credit: £%.2f", credit / 100))
            print("You lose! Not enough credit left to spin again.")
            break
        end

        print()
        ::continue::
    end 
end

main()
