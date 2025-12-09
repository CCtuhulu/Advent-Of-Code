lines = File.readlines("input.txt",chomp: true)

divider = lines.index("")

ranges = lines[..divider]
ingredients = lines[divider+1..]

result = 0

ingredients.each do |i|
    spoil = true
    ranges.each do |j|
            min,max = j.split("-")
            if min.to_i <= i.to_i and i.to_i <= max.to_i
                            spoil = false
                            break
            end
    end

    if !spoil
            result += 1
    end
end

puts result