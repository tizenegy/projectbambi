clear all
close all
clc

figure
axis equal
hold on

color = ['r' 'g' 'y' 'b' 'c' 'k'];

for i=1:6
    [num, txt, raw]=xlsread('contours.xlsx',i);
    
    % Init group value and sequence number
    group(i) = i;
    verticalSequenceNumber(i) = 1;
    horizontalSequenceNumber(i) = 1;
    
    % Detected Element Type
    elementType_str(i) = txt(1);
    if strcmp('circle',elementType_str(i)) == 1
        elementType_uint(i) = 3;
    elseif strcmp('rectangle',elementType_str(i)) == 1
        elementType_uint(i) = 1;
    elseif strcmp('triangle',elementType_str(i)) == 1
        elementType_uint(i) = 2;
    else
        error('Element Type Detection Error ! ! !');
    end
    
    % Element Position Data
    centerPoint(i,:) = [num(1,3) num(1,4)];
    positionData.x = num(2:length(num),1); 
    positionData.y = num(2:length(num),2);
    
    % Estimated Element Representation
    elementHight(i) = max(positionData.y) - min(positionData.y);
    elementLength(i) = max(positionData.x) - min(positionData.x);
    
%     if elementType_uint(i) == 0 % circle
%         circleCenter = centerPoint(i);
%         circleRadius = mean(elementHight(i), elementLength(i))/2;
%         triangle_flag = 0;
%     elseif elementType_uint(i) == 1 % rectangle
%         rectangleCenter = centerPoint(i);
%         rectangleHight = elementHight(i);
%         rectangleLength = elementLength(i);
%         triangle_flag = 0;
%     elseif elementType_uint(i) == 2 % triangle
%         triangle_flag = 1;
%     else
%         triangle_flag = 0;
%     end
    
    % Grouping the elements
    if i ~= 1
        for j=1:(i-1)
            % If y-value of center point lies within the range of the j-th
            % element, the i-th element and the j-th element should be
            % grouped together
            if ((centerPoint(i,2) <= (centerPoint(j,2)+(elementHight(j)/2))) && (centerPoint(i,2) >= (centerPoint(j,2)-(elementHight(j)/2))))
                group(i) = group(j);
            end
        end
    else
        % NOP
    end
    
    % Visualize
    plot(positionData.x,positionData.y, color(i))
    plot(centerPoint(i,1),centerPoint(i,2), [color(i) 'x'])
    text(centerPoint(i,1)-10, centerPoint(i,2)+10, ['\bf \fontsize{16} Group ' num2str(group(i))], 'Color', color(i))
%     text(centerPoint(i,1), centerPoint(i,2)-10, ['\bf \fontsize{16}' num2str(i)], 'Color', color(i))
    
%     if elementType_uint(i) == 0 % circle
%         viscircles(circleCenter,circleRadius, 'Color', color(i));
%     elseif elementType_uint(i) == 1 % rectangle
%         pos = [(rectangleCenter(1)-(rectangleLength/2)) (rectangleCenter(2)-(rectangleHight/2)) rectangleLength rectangleHight];
%         rectangle('Position', pos, 'EdgeColor', color(i));
%     elseif elementType_uint(i) == 2 % triangle
%         text(centerPoint(i,1)-10, centerPoint(i,2)+10, '\bf \fontsize{16} !\^!', 'Color', color(i))
%     end
end

%% Determine placement of output types "rectangle" (1), "triangle" (2), "circle" (3)

% Determine vertical sequence number (which element is highest/ lowest on the screen)
for i=1:length(elementType_uint)
    for j=1:length(elementType_uint)
        if ((i ~= j) && (centerPoint(i,2) > centerPoint(j,2)))
            verticalSequenceNumber(i) = verticalSequenceNumber(i) + 1;
        end
    end
end

% Determine horizontal sequence number (which element is more to the left/ right on the screen)
for i=1:length(elementType_uint)
    for j=1:length(elementType_uint)
        if ((i ~= j) && (group(i) == group(j)) && (centerPoint(i,1) > centerPoint(j,1)))
            horizontalSequenceNumber(i) = horizontalSequenceNumber(i) + 1;
        end
    end
end

% Init (general) sequence number
sequenceNumber = verticalSequenceNumber;

% Set every group members vertical sequence number to the sequence number of the
% group
for i=1:length(elementType_uint)
    for j=1:length(elementType_uint)
        if ((i ~= j) && (group(i) == group(j)))
            verticalSequenceNumber(i) = min(verticalSequenceNumber(i),verticalSequenceNumber(j));
            verticalSequenceNumber(j) = min(verticalSequenceNumber(i),verticalSequenceNumber(j));
        else
            %NOP
        end
    end
end

% Adjust sequence number of group members according to their horizontal
% sequence number
sequenceNumbersInGroup = ones(length(elementType_uint),max(horizontalSequenceNumber))*99;
for i=1:length(elementType_uint)
   sequenceNumbersInGroup(group(i),horizontalSequenceNumber(i)) = sequenceNumber(i);
end

for i=1:length(elementType_uint)
    sequenceNumber(i) = min(sequenceNumbersInGroup(group(i),:)) + horizontalSequenceNumber(i) - 1;
end


%% Determine placement of output type "group"
for i=1:length(elementType_uint)
    for j=1:length(elementType_uint)
        if sequenceNumber(j) == i
            groupOfSequenceItems(i) = group(j);
        end
    end
end

grouping = [];
groupSequence = [];
membersInGroup = 1;
for i=1:(length(groupOfSequenceItems)-1)
    if groupOfSequenceItems(i) == groupOfSequenceItems(i+1)
        membersInGroup = membersInGroup + 1;
    else
        grouping = [grouping membersInGroup];
        groupSequence = [groupSequence groupOfSequenceItems(i)];
        membersInGroup = 1;
    end
end
if groupOfSequenceItems(length(groupOfSequenceItems)) ~= groupOfSequenceItems(length(groupOfSequenceItems)-1)
    grouping = [grouping 1];
    groupSequence = [groupSequence groupOfSequenceItems(length(groupOfSequenceItems))];
else
    %NOP
end


%% Export to txt file
out = [];
for k=1:length(groupSequence)
    if grouping(k) ~= 1
        out = [out; 0 groupSequence(k)]; % "Group(groupID)"
%         fprintf('Group(%u)\n', groupSequence(k))
    end
    if k==1
        startingValue = 1;
    else
        startingValue = 1+sum(grouping(1:(k-1)));
    end
    for i = startingValue:(startingValue + grouping(k) - 1)
        for j=1:length(elementType_uint)
            if sequenceNumber(j) == i
%                 fprintf('%s(%u)\n', char(elementType_str(j)), group(j))
                out = [out; elementType_uint(j) group(j)];
            end
        end
    end
end

out
