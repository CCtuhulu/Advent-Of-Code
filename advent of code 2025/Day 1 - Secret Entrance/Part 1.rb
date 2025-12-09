lines = File.readlines("input.txt", chomp: true)

pos = 50
result = 0
lines.each do |i|
  move = i.slice!(0)
  num = i[0..-1].to_i
  if move == "R"
    pos += num
    pos %= 100
  elsif move == "L"
    if pos >= num
      pos -= num
    else
      pos = (pos-num)%100
    end
  end

  if pos == 0
    result += 1
  end
end

puts result