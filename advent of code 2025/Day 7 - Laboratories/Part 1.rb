lines = File.readlines("input.txt",chomp:true)

start = lines[0].index("S")
lines[1][start] = "|"
splits = 0

(2...lines.length).each do |i|
  
  (0...lines[i].length).each do |j|
    
    if lines[i][j] == "^"
      if lines[i-1][j] == "|"
        
        splits += 1

        if j>0 and lines[i][j-1] != "^"
          lines[i][j-1] = "|"
        end

        if j<lines[i].length and lines[i][j+1] != "^"
          lines[i][j+1] = "|"
        end

      end
    
    elsif lines[i][j] == "."
      if lines[i-1][j] == "|"
        lines[i][j] = "|"
      end
    end

  end

end

puts splits