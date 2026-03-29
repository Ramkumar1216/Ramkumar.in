INSERT INTO services_service (title, slug, description, price, icon, features, created_at) 
VALUES ('Data Analytics', 'data-analytics', 'Transform your business data into actionable insights with advanced analytics, dashboards, and reporting. I identify hidden revenue opportunities and build systems that drive measurable results.', '₹25,000+', '📊', 'Custom dashboards, Data analysis, Weekly reports, Expert consultation, Revenue impact analysis, Dashboard training', datetime('now'));

INSERT INTO services_service (title, slug, description, price, icon, features, created_at) 
VALUES ('Digital Marketing', 'digital-marketing', 'Drive growth with strategic digital marketing campaigns, SEO optimization, and social media management. I focus on measurable ROI and sustainable customer acquisition.', '₹20,000+', '🎯', 'SEO optimization, Social media management, Content strategy, Campaign management, Conversion optimization, Analytics tracking', datetime('now'));

INSERT INTO services_service (title, slug, description, price, icon, features, created_at) 
VALUES ('Web Development', 'web-development', 'Build responsive, modern websites with Django and React that drive conversions and engage users. I create scalable solutions that grow with your business.', '₹35,000+', '💻', 'Responsive design, SEO friendly, CMS integration, Mobile optimized, Performance optimization, Security hardening', datetime('now'));

SELECT title, slug FROM services_service;
