stats = csvread('SkillsSet.csv');
num_skills = size(stats, 2);
skills = cell(num_skills, 1);
for i = 1:num_skills
    column = stats(:,i);
    average = mean(column);
    standard_deviation = std(column);
    
    column = column - average;
    column = column/standard_deviation;
    
    skills{i} = diag(stats(:, i)');
    
end


num_players = size(stats, 1);
edgeMatrix = csvread('matrixForFPL.txt');


currentPlayTeam = [15 8 4 6 12 11 5 7 1 13 14];
memberToReplace = currentPlayTeam(2);
score = GraphSimilarity(edgeMatrix, skills, currentPlayTeam, memberToReplace, 'false');
[~,idx] = sort(score(:,1),'ascend')
score2 = score(idx,:);
disp(score2)
