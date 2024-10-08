meanI = 60000;
sdI = 8000;
exD = 6.25e-5;
income_values = linspace(meanI -4*sdI, meanI +4*sdI, 1000);
income_pdf = normpdf(income_values, meanI, sdI);
expenses_values = linspace(0, 200000, 1000);
expenses_pdf = exppdf(expenses_values, 1 / exD);
figure;
plot(income_values, income_pdf, 'b', 'LineWidth', 2);
hold on;
plot(expenses_values, expenses_pdf, 'r', 'LineWidth', 2);
xlabel('Amount');
ylabel('Density');
title('Density Functions for Income and Expenses');
legend('Income (Normal)', 'Expenses (Exponential)');
grid on;
hold off;
