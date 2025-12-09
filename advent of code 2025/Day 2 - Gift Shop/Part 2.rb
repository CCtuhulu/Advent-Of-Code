line = File.readlines("input.txt", chomp: true)

ranges = line[0].split(",")

result = 0

ranges.each do |range|
  bot, top = range.split("-").map(&:to_i)
  (bot..top).each do |i|
    if i.to_s.match?(/^(\d+)\1+$/)
      result+=i.to_i
    end
  end
end

puts result