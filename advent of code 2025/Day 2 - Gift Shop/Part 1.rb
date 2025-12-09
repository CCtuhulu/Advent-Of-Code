line = File.readlines("input.txt", chomp: true)

ranges = line[0].split(",")

result = 0

ranges.each do |range|
  bot, top = range.split("-").map(&:to_i)
  (bot..top).each do |i|
    i = i.to_s
    len = i.length / 2
    if i[0..(len-1)] == i[len..] and i.length > 1
      result += i.to_i
    end
  end
end

puts result