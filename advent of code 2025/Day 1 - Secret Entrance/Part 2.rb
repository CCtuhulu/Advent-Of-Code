lines = File.readlines("input.txt", chomp: true)

pos = 50
result = 0
lines.each do |i|
  move = i.slice!(0)
  num = i[0..-1].to_i
  if move == "R"
    pos += num
    result += (pos/100.0).floor
    pos %= 100
  elsif move == "L"
    if pos >= num
      pos -= num
      if pos == 0
        result += 1
      end
    else
      if pos == 0
        result -= 1
      end
      pos -= num
      result += (pos/100.0).abs.floor + 1
      pos %= 100
    end
  end
end

puts result