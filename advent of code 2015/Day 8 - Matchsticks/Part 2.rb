lines = File.readlines("input.txt",chomp: true)


x = 0
l = 0
lines.each do |line|
    len = line.length
    l += len
    x += len
    hexa = ["a","b","c","d","e","f","0","1","2","3","4","5","6","7","8","9"]
    i = 0
    inside = false
    while i < len
        
      if line[i] == "\""
        inside = !inside
        x += 2

      elsif line[i] == "\\"
        if i < (len-1) and (line[i+1] == "\\" or line[i+1] == "\"")
          i += 1
          x += 2
        elsif i < (len-3) and line[i+1] == "x" and hexa.include?(line[i+2]) and hexa.include?(line[i+3])
          i += 3
          x += 1
        end 

      end

      i += 1

    end
end

puts x-l
