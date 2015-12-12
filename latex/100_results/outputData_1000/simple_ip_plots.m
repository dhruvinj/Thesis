clear all; close all; clc ;
ip_raw_chain

% Chain plots -------------------------------------------------------------
for i=1:size(ip_mh_rawChain_unified,1)
id_raw(i)=i;
end
 
fprintf(1,' Plotting chains - filtered  <press any key>\n');
plot(id_raw,ip_mh_rawChain_unified);

ylabel('Parameter values','fontname', 'Times', 'fontsize',20);
xlabel('Number of positions','fontname', 'Times', 'fontsize',20);
title('DRAM MCMC Chain Positions (filtered)','fontname', 'Times', 'fontsize',20);
h=legend('\theta_1','\theta_2','location','northeast');
% axis([0 2000 -8 6]);
set(h,'fontname', 'Times', 'fontsize',16);
set(gca,'FontSize',16);
print -dpng simple_ip_chain_pos_filt.png
figure

% Histogram plots ---------------------------------------------------------
% RAW
fprintf(1,' Plotting histogram - raw  <press any key>\n');
nbins=250;
hist(ip_mh_rawChain_unified(:,1),nbins)
h = findobj(gca,'Type','patch');
title('Parameters Histogram (raw chain, nbins=20)','fontname', 'Times', 'fontsize',20);
xlabel('Parameters','fontname', 'Times', 'fontsize',20);
grid on;
print -dpng simple_ip_hist_raw.png
figure



% KDE plots ---------------------------------------------------------------
% RAW
fprintf(1,' Plotting KDE - raw  <press any key>\n');
[f,x] = ksdensity(ip_mh_rawChain_unified(:,1),'function','pdf');

x_p1=sort(ip_mh_rawChain_unified(:,1)); %analytical
f_p1=(exp(-(x_p1+1).*(x_p1+1)/8))/2/sqrt(2*pi);
x_p2=sort(ip_mh_rawChain_unified(:,1));
f_p2=(exp(-(x_p2-2).*(x_p2-2)/2))/sqrt(2*pi);

plot(x,f,'b','linewidth',4);
hold;
plot(x_p1,f_p1,'--k',x_p2,f_p2,'-k','linewidth',2);

h=legend('\theta_1', 'location', 'northwest');
title('Parameter Kernel Density Estimation (raw chain)','fontname', 'Times', 'fontsize',20);
xlabel('\theta_1','fontname', 'Times', 'fontsize',20);
ylabel('KDE','fontname', 'Times', 'fontsize',20);
grid minor;
set(gca,'FontSize',16);
print -dpng simple_ip_kde_raw.png
figure




% CDF plots ---------------------------------------------------------------
fprintf(1,' Plotting CDF - raw  <press any key>\n');
[f,xi] = ksdensity(ip_mh_rawChain_unified(:,1),'function','cdf');
plot(xi,f,'b','linewidth',3);
h=legend('\theta_1','location','southeast');
title('Parameter Cumulative Distribution Function (raw chain)','fontname', 'Times', 'fontsize',20);
xlabel('\theta_1 ','fontname', 'Times', 'fontsize',20);
ylabel('CDF','fontname', 'Times', 'fontsize',20);
grid minor;
set(gca,'FontSize',16);
print -dpng simple_ip_cdf_raw.png
figure


ip_raw_chain_loglikelihood

figure; scatter(ip_mh_rawChain_unified,ip_logLike_unified)
title('Parameter Probability Distribution Function (raw chain)','fontname', 'Times', 'fontsize',20);
xlabel('\theta_1 ','fontname', 'Times', 'fontsize',20);
ylabel('PDF','fontname', 'Times', 'fontsize',20);
print -dpng ip_logLike_unified.png



