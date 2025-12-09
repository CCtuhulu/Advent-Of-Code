lines = File.readlines("input.txt",chomp:true)
arr = []

(1...lines.length).each do |i|

    x1,y1,z1 = lines[i].split(",")

    (0...i).each do |j|
            x2,y2,z2 = lines[j].split(",")

            arr << [Math.sqrt((x1.to_i-x2.to_i)**2 + (y1.to_i-y2.to_i)**2 + (z1.to_i-z2.to_i)**2),lines[i],lines[j]]
    end
end
arr.sort_by! {|e| e[0]}

circuits = []
circuits << [arr[0][1], arr[0][2]]

(1...1000).each do |i|
    junc1 = arr[i][1]
    junc2 = arr[i][2]
    jpos1 = -1
    jpos2 = -1
    circuits.each_with_index do |circuit,j|
        jindex1 = circuit.index(junc1)
        jindex2 = circuit.index(junc2)
        if jindex1
                    jpos1 = j
        end
        if jindex2
                    jpos2 = j
        end

        if jpos1 != -1 and jpos2 != -1
                    break
        end
    end

    if jpos1 == -1 and jpos2 == -1
            circuits << [junc1,junc2]
    elsif jpos1 == -1 and jpos2 != -1
            circuits[jpos2] << junc1
    elsif jpos1 != -1 and jpos2 == -1
            circuits[jpos1] << junc2
    elsif jpos1 == jpos2
            next
    elsif jpos1 != jpos2
            merged = circuits[jpos1] + circuits[jpos2]
            hi = [jpos1, jpos2].max
            lo = [jpos1, jpos2].min

            circuits.delete_at(hi)
            circuits.delete_at(lo)
            circuits << merged 
    end
end
circuits.sort_by! {|e| -e.length}
print circuits
print circuits[0].length * circuits[1].length * circuits[2].length