lines = File.readlines("input.txt",chomp:true)

result = 0

(1...lines.length-1).each do |i|
  x1,y1 = lines[i].split(",")
  x1 = x1.to_i
  y1 = y1.to_i
  (0...lines.length-2).each do |j|
    x2,y2 = lines[j].split(",")
    x2 = x2.to_i
    y2 = y2.to_i
    surface = ((x1-x2).abs+1) * ((y1-y2).abs+1)
    if surface > result
        result = surface    
    end
  end
end

puts result